#!/usr/bin/env python3
"""
Script to fix broken image links in Obsidian vault by removing hash suffixes from paths.

This script finds all markdown files and removes hash suffixes like '%20c7c62f76a0064b409316869b31060490'
from image link paths that were broken after mass renaming of folders and files.
"""

import os
import re
import glob

def fix_image_links_in_vault(vault_path):
    """
    Fix all broken image links in the Obsidian vault by removing hash suffixes.
    
    Args:
        vault_path (str): Path to the Obsidian vault directory
    """
    
    # Pattern to match image links with hash suffixes
    # Matches: ![text](path/folder hash32chars/filename)
    # where hash32chars is a 32-character hex string
    # The hash is preceded by a space character
    pattern = r'(!\[.*?\]\([^)]*?)\s([a-f0-9]{32})(\/[^)]*?\))'
    
    # Find all markdown files
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    
    print(f"Found {len(md_files)} markdown files to process...")
    
    total_fixes = 0
    files_modified = 0
    
    for md_file in md_files:
        try:
            # Read the file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find and replace broken links
            new_content, num_replacements = re.subn(pattern, r'\1\3', content)
            
            if num_replacements > 0:
                # Write back the fixed content
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                files_modified += 1
                total_fixes += num_replacements
                print(f"Fixed {num_replacements} links in: {os.path.relpath(md_file, vault_path)}")
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print("\nCompleted!")
    print(f"Files modified: {files_modified}")
    print(f"Total links fixed: {total_fixes}")

def preview_fixes(vault_path, max_preview=10):
    """
    Preview what fixes would be made without actually changing files.
    
    Args:
        vault_path (str): Path to the Obsidian vault directory
        max_preview (int): Maximum number of examples to show
    """
    
    pattern = r'(!\[.*?\]\([^)]*?)(%20[a-f0-9]{32})(\/[^)]*?\))'
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    
    print("Preview of fixes that would be made:")
    print("=" * 60)
    
    examples_shown = 0
    
    for md_file in md_files:
        if examples_shown >= max_preview:
            break
            
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            matches = re.finditer(pattern, content)
            for match in matches:
                if examples_shown >= max_preview:
                    break
                    
                original = match.group(0)
                fixed = re.sub(pattern, r'\1\3', original)
                
                print(f"File: {os.path.relpath(md_file, vault_path)}")
                print(f"Before: {original}")
                print(f"After:  {fixed}")
                print("-" * 40)
                
                examples_shown += 1
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    print(f"\nShowing {examples_shown} examples (use --fix to apply changes)")

if __name__ == "__main__":
    import sys
    
    # Set the vault path
    vault_path = r"c:\Users\daanquin\Obsidian\new"
    
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        # Actually fix the files
        fix_image_links_in_vault(vault_path)
    else:
        # Just preview what would be fixed
        preview_fixes(vault_path)
