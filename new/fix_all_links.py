#!/usr/bin/env python3
"""
Complete script to fix all Obsidian image links with hash suffixes.
This script will find ALL markdown files and fix the broken links.
"""

import os
import re
import sys

def fix_all_obsidian_links(vault_path, actually_fix=False):
    """
    Find and fix all broken image links in the Obsidian vault.
    """
    
    pattern = r'(!\[.*?\]\([^)]*?)(%20[a-f0-9]{32})(\/[^)]*?\))'
    
    total_files_processed = 0
    total_files_with_issues = 0
    total_links_fixed = 0
    
    print("Scanning all markdown files for broken image links...")
    print("=" * 60)
    
    # Walk through all directories
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                total_files_processed += 1
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, vault_path)
                
                try:
                    # Read file with error handling for encoding issues
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    
                    # Find all matches
                    matches = list(re.finditer(pattern, content))
                    
                    if matches:
                        total_files_with_issues += 1
                        print(f"\n📁 {relative_path}")
                        print(f"   Found {len(matches)} broken link(s):")
                        
                        for i, match in enumerate(matches):
                            original = match.group(0)
                            fixed = re.sub(pattern, r'\1\3', original)
                            print(f"   {i+1}. {original}")
                            print(f"      → {fixed}")
                        
                        if actually_fix:
                            # Apply the fix
                            new_content = re.sub(pattern, r'\1\3', content)
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            total_links_fixed += len(matches)
                            print(f"   ✅ Fixed {len(matches)} links")
                        
                        # Show progress every 10 problematic files
                        if total_files_with_issues % 10 == 0:
                            print(f"\n📊 Progress: {total_files_processed} files scanned, {total_files_with_issues} with issues...")
                
                except Exception as e:
                    print(f"❌ Error processing {relative_path}: {e}")
    
    # Final summary
    print("\n" + "=" * 60)
    print("📋 SUMMARY:")
    print(f"   Total files scanned: {total_files_processed}")
    print(f"   Files with broken links: {total_files_with_issues}")
    if actually_fix:
        print(f"   Total links fixed: {total_links_fixed}")
        print("   ✅ All fixes have been applied!")
    else:
        print("   🔍 This was a preview run.")
        print("   Run with --fix to apply the changes.")

if __name__ == "__main__":
    vault_path = "/mnt/c/Users/daanquin/Obsidian/new"
    
    # Check if we should actually fix or just preview
    actually_fix = len(sys.argv) > 1 and sys.argv[1] == "--fix"
    
    if actually_fix:
        print("🔧 FIXING MODE: Will actually modify files!")
        confirm = input("Are you sure you want to proceed? (y/N): ")
        if confirm.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)
    else:
        print("🔍 PREVIEW MODE: Will show what would be fixed")
    
    fix_all_obsidian_links(vault_path, actually_fix)
