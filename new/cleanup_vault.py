#!/usr/bin/env python3
"""
Comprehensive script to:
1. Rename files and folders to remove hash suffixes
2. Update all markdown references to match the new names
"""

import os
import re
import shutil
import glob

def find_paths_with_hashes(vault_path):
    """Find all files and directories with hash suffixes in their names."""
    hash_pattern = r'[a-f0-9]{32}'
    paths_with_hashes = []
    
    print("🔍 Scanning for files and folders with hash suffixes...")
    
    for root, dirs, files in os.walk(vault_path):
        # Check directories
        for dir_name in dirs:
            if re.search(hash_pattern, dir_name):
                full_path = os.path.join(root, dir_name)
                paths_with_hashes.append(('dir', full_path))
        
        # Check files
        for file_name in files:
            if re.search(hash_pattern, file_name):
                full_path = os.path.join(root, file_name)
                paths_with_hashes.append(('file', full_path))
    
    return paths_with_hashes

def create_clean_name(path_with_hash):
    """Remove hash suffix from a path name."""
    # Pattern to match: "name hash32chars" or "name%20hash32chars"
    hash_pattern = r'(\s|%20)[a-f0-9]{32}'
    
    # Get just the filename/dirname
    parent_dir = os.path.dirname(path_with_hash)
    name = os.path.basename(path_with_hash)
    
    # Remove the hash suffix
    clean_name = re.sub(hash_pattern, '', name)
    
    return os.path.join(parent_dir, clean_name)

def rename_paths_with_hashes(paths_with_hashes, dry_run=True):
    """Rename all paths to remove hash suffixes."""
    rename_mappings = []
    
    # Sort by depth (deepest first) to avoid renaming parent before children
    paths_with_hashes.sort(key=lambda x: x[1].count(os.sep), reverse=True)
    
    print(f"\n📝 Planning renames ({'DRY RUN' if dry_run else 'ACTUAL'}):")
    print("=" * 80)
    
    for path_type, old_path in paths_with_hashes:
        new_path = create_clean_name(old_path)
        
        if old_path != new_path:
            print(f"{path_type.upper()}: {os.path.basename(old_path)}")
            print(f"    → {os.path.basename(new_path)}")
            
            if not dry_run:
                try:
                    if os.path.exists(new_path):
                        print(f"    ⚠️  Target already exists, skipping: {new_path}")
                        continue
                    
                    # Create parent directory if it doesn't exist
                    os.makedirs(os.path.dirname(new_path), exist_ok=True)
                    
                    # Rename the path
                    shutil.move(old_path, new_path)
                    print("    ✅ Renamed successfully")
                    
                except Exception as e:
                    print(f"    ❌ Error renaming: {e}")
                    continue
            
            rename_mappings.append((old_path, new_path))
    
    return rename_mappings

def update_markdown_references(vault_path, rename_mappings, dry_run=True):
    """Update all markdown files to reference the new renamed paths."""
    print(f"\n🔗 Updating markdown references ({'DRY RUN' if dry_run else 'ACTUAL'}):")
    print("=" * 80)
    
    # Find all markdown files
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    
    files_updated = 0
    total_replacements = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            
            file_replacements = 0
            
            # Apply all rename mappings to this file's content
            for old_path, new_path in rename_mappings:
                # Convert absolute paths to relative paths that might appear in markdown
                old_rel = os.path.relpath(old_path, vault_path)
                new_rel = os.path.relpath(new_path, vault_path)
                
                # Replace forward slash version (common in markdown)
                old_rel_forward = old_rel.replace('\\', '/')
                new_rel_forward = new_rel.replace('\\', '/')
                
                # Count replacements
                count_before = len(re.findall(re.escape(old_rel_forward), content, re.IGNORECASE))
                if count_before > 0:
                    content = content.replace(old_rel_forward, new_rel_forward)
                    file_replacements += count_before
                
                # Also try with URL encoding
                old_rel_encoded = old_rel_forward.replace(' ', '%20')
                new_rel_encoded = new_rel_forward.replace(' ', '%20')
                
                count_encoded = len(re.findall(re.escape(old_rel_encoded), content, re.IGNORECASE))
                if count_encoded > 0:
                    content = content.replace(old_rel_encoded, new_rel_encoded)
                    file_replacements += count_encoded
            
            if file_replacements > 0:
                rel_md_file = os.path.relpath(md_file, vault_path)
                print(f"📄 {rel_md_file}: {file_replacements} reference(s) updated")
                
                if not dry_run:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                
                files_updated += 1
                total_replacements += file_replacements
        
        except Exception as e:
            print(f"❌ Error processing {md_file}: {e}")
    
    print(f"\n📊 Summary: {files_updated} files updated, {total_replacements} total replacements")

def main():
    vault_path = "/mnt/c/Users/daanquin/Obsidian/new"
    
    print("🗂️  OBSIDIAN HASH CLEANUP TOOL")
    print("=" * 50)
    print("This script will:")
    print("1. Find all files/folders with hash suffixes")
    print("2. Rename them to remove the hashes")
    print("3. Update all markdown references")
    print()
    
    # Step 1: Find paths with hashes
    paths_with_hashes = find_paths_with_hashes(vault_path)
    
    if not paths_with_hashes:
        print("✅ No files or folders with hash suffixes found!")
        return
    
    print(f"Found {len(paths_with_hashes)} items with hash suffixes")
    
    # Step 2: Show what would be renamed (dry run)
    rename_mappings = rename_paths_with_hashes(paths_with_hashes, dry_run=True)
    
    if not rename_mappings:
        print("No renames needed.")
        return
    
    # Step 3: Show what markdown updates would happen (dry run)
    update_markdown_references(vault_path, rename_mappings, dry_run=True)
    
    # Step 4: Ask for confirmation
    print("\n" + "=" * 50)
    print("⚠️  IMPORTANT: This will permanently rename files and folders!")
    print("Make sure you have a backup of your vault before proceeding.")
    
    confirm = input("\nProceed with actual renaming and updates? (y/N): ")
    
    if confirm.lower() == 'y':
        print("\n🔧 APPLYING CHANGES...")
        
        # Actually perform the renames
        actual_mappings = rename_paths_with_hashes(paths_with_hashes, dry_run=False)
        
        # Update markdown references
        update_markdown_references(vault_path, actual_mappings, dry_run=False)
        
        print("\n✅ ALL DONE! Your vault has been cleaned up.")
        print("   - Files and folders renamed to remove hash suffixes")
        print("   - All markdown references updated")
    else:
        print("❌ Operation cancelled.")

if __name__ == "__main__":
    main()
