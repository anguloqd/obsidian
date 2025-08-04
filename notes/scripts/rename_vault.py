#!/usr/bin/env python3
"""
Script to rename all files and folders in the Obsidian vault:
- Replace spaces with underscores
- Convert capital letters to lowercase
- Update internal references in markdown files
"""

import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

def normalize_name(name):
    """
    Convert a filename/foldername to lowercase and replace spaces with underscores.
    """
    # Replace spaces with underscores
    normalized = name.replace(' ', '_')
    # Convert to lowercase
    normalized = normalized.lower()
    return normalized

def get_all_paths(root_dir):
    """
    Get all file and directory paths, sorted by depth (deepest first for renaming).
    """
    all_paths = []
    
    for root, dirs, files in os.walk(root_dir):
        # Add files
        for file in files:
            if file != 'rename_vault.py':  # Skip this script
                all_paths.append(Path(root) / file)
        
        # Add directories
        for dir_name in dirs:
            all_paths.append(Path(root) / dir_name)
    
    # Sort by depth (deepest first) so we rename children before parents
    all_paths.sort(key=lambda p: len(p.parts), reverse=True)
    return all_paths

def create_rename_mapping(all_paths):
    """
    Create a mapping of old paths to new paths.
    """
    rename_mapping = {}
    
    for old_path in all_paths:
        parts = list(old_path.parts)
        new_parts = []
        
        for part in parts:
            if part == 'c:' or part == '\\' or ':\\' in part:
                new_parts.append(part)
            else:
                new_parts.append(normalize_name(part))
        
        new_path = Path(*new_parts)
        if old_path != new_path:
            rename_mapping[old_path] = new_path
    
    return rename_mapping

def update_markdown_references(file_path, rename_mapping):
    """
    Update references in markdown files to use the new names.
    This handles images, PDFs, and all other attachments.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Helper function to normalize any file path
        def normalize_path(path_part):
            """Normalize a file path by converting spaces to underscores and making lowercase"""
            # Decode URL encoding if present (handles %20 for spaces, etc.)
            path_part = unquote(path_part)
            
            # Split path into parts and normalize each part
            if path_part.startswith('new/'):
                # Convert absolute reference starting with 'new/'
                relative_path = path_part[4:]  # Remove 'new/' prefix
                parts = relative_path.split('/')
                new_parts = [normalize_name(part) for part in parts]
                return 'new/' + '/'.join(new_parts)
            else:
                # Handle relative paths
                parts = path_part.split('/')
                new_parts = [normalize_name(part) for part in parts]
                return '/'.join(new_parts)
        
        # 1. Update image references like ![description](path/to/image.png)
        def replace_attachment_ref(match):
            description = match.group(1)
            path_part = match.group(2)
            
            # Skip external URLs
            if path_part.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                return match.group(0)
            
            new_path = normalize_path(path_part)
            return f'![{description}]({new_path})'
        
        # Pattern for markdown image/attachment references
        content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_attachment_ref, content)
        
        # 2. Update wiki-style links [[Page Name]] or [[Page Name|Display Text]]
        def replace_wiki_link(match):
            link_content = match.group(1)
            if '|' in link_content:
                link_target, display_text = link_content.split('|', 1)
                # Only normalize the target, keep display text as is
                return f'[[{normalize_name(link_target)}|{display_text}]]'
            else:
                return f'[[{normalize_name(link_content)}]]'
        
        content = re.sub(r'\[\[([^\]]+)\]\]', replace_wiki_link, content)
        
        # 3. Update regular markdown links [text](path) - for PDFs and other files
        def replace_md_link(match):
            text = match.group(1)
            path_part = match.group(2)
            
            # Skip external URLs
            if path_part.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                return match.group(0)
            
            new_path = normalize_path(path_part)
            return f'[{text}]({new_path})'
        
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_md_link, content)
        
        # 4. Update Obsidian-style attachment links ![[filename.ext]]
        def replace_obsidian_attachment(match):
            filename = match.group(1)
            # Skip if it looks like an external reference
            if filename.startswith(('http://', 'https://')):
                return match.group(0)
            return f'![[{normalize_name(filename)}]]'
        
        content = re.sub(r'!\[\[([^\]]+)\]\]', replace_obsidian_attachment, content)
        
        # 5. Update any remaining file paths in the content (be more aggressive)
        # This catches things like bare file paths or other formats
        def replace_bare_paths(match):
            full_match = match.group(0)
            path_part = match.group(1)
            
            # Skip if it's already been processed or is an external URL
            if path_part.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                return full_match
            
            # Only process if it contains our vault structure
            if 'new/' in path_part or any(folder in path_part for folder in ['uga/', 'ensimag/', '_assets/']):
                new_path = normalize_path(path_part)
                return full_match.replace(path_part, new_path)
            
            return full_match
        
        # Pattern to catch remaining file paths (more conservative)
        content = re.sub(r'(\S*(?:new/|uga/|ensimag/|_assets/)\S*)', replace_bare_paths, content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated references in: {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error updating references in {file_path}: {e}")
        return False

def rename_files_and_folders(rename_mapping):
    """
    Rename files and folders according to the mapping.
    """
    renamed_count = 0
    
    for old_path, new_path in rename_mapping.items():
        try:
            if old_path.exists():
                # Create parent directories if they don't exist
                new_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Rename the file/folder
                shutil.move(str(old_path), str(new_path))
                print(f"Renamed: {old_path} -> {new_path}")
                renamed_count += 1
        except Exception as e:
            print(f"Error renaming {old_path} to {new_path}: {e}")
    
    return renamed_count

def main():
    """
    Main function to rename all files and folders in the Obsidian vault.
    """
    # Use the current working directory since we'll run from the vault directory
    root_dir = Path(".")
    
    if not root_dir.exists():
        print(f"Error: Directory {root_dir} does not exist")
        return
    
    print("Starting Obsidian vault renaming process...")
    print(f"Root directory: {root_dir}")
    
    # Get all paths
    print("Scanning directory structure...")
    all_paths = get_all_paths(root_dir)
    print(f"Found {len(all_paths)} files and folders")
    
    # Create rename mapping
    print("Creating rename mapping...")
    rename_mapping = create_rename_mapping(all_paths)
    print(f"Will rename {len(rename_mapping)} items")
    
    if not rename_mapping:
        print("No files or folders need renaming!")
        return
    
    # Show preview
    print("\nPreview of changes:")
    for i, (old_path, new_path) in enumerate(list(rename_mapping.items())[:10]):
        print(f"  {old_path.name} -> {new_path.name}")
    if len(rename_mapping) > 10:
        print(f"  ... and {len(rename_mapping) - 10} more")
    
    # Confirm with user
    response = input("\nProceed with renaming? (y/N): ")
    if response.lower() != 'y':
        print("Renaming cancelled.")
        return
    
    # Rename files and folders
    print("\nRenaming files and folders...")
    renamed_count = rename_files_and_folders(rename_mapping)
    
    # Update markdown references
    print("\nUpdating markdown file references...")
    updated_files = 0
    total_md_files = 0
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                total_md_files += 1
                file_path = Path(root) / file
                if update_markdown_references(file_path, rename_mapping):
                    updated_files += 1
    
    print("\nRenaming complete!")
    print(f"- Renamed {renamed_count} files and folders")
    print(f"- Updated references in {updated_files} out of {total_md_files} markdown files")

if __name__ == "__main__":
    main()
