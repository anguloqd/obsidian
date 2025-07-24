#!/usr/bin/env python3
"""
Script to fix broken image links in Obsidian vault by removing hash suffixes from paths.
"""

import os
import re
import glob

def fix_obsidian_image_links(vault_path, preview_only=True):
    """
    Fix all broken image links by removing hash suffixes.
    
    Pattern to match: ![text](path/folder%20hash32chars/filename)
    where hash32chars is a 32-character hex string
    """
    
    # This pattern matches:
    # 1. Image link start: ![anything](
    # 2. Path part before hash: any characters 
    # 3. URL-encoded space + 32-char hex hash: %20[a-f0-9]{32}
    # 4. Rest of path: /filename)
    pattern = r'(!\[.*?\]\([^)]*?)(%20[a-f0-9]{32})(\/[^)]*?\))'
    
    # Find all markdown files
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    
    print(f"Found {len(md_files)} markdown files to process...")
    
    total_fixes = 0
    files_modified = 0
    examples_shown = 0
    max_examples = 10
    
    for md_file in md_files:
        try:
            # Read the file
            with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find matches
            matches = list(re.finditer(pattern, content))
            
            if matches:
                if preview_only:
                    print(f"\nFile: {os.path.relpath(md_file, vault_path)}")
                    for match in matches:
                        if examples_shown >= max_examples:
                            break
                        original = match.group(0)
                        fixed = re.sub(pattern, r'\1\3', original)
                        print(f"  Before: {original}")
                        print(f"  After:  {fixed}")
                        examples_shown += 1
                    if examples_shown >= max_examples:
                        break
                else:
                    # Actually fix the content
                    new_content = re.sub(pattern, r'\1\3', content)
                    
                    # Write back the fixed content
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    files_modified += 1
                    total_fixes += len(matches)
                    print(f"Fixed {len(matches)} links in: {os.path.relpath(md_file, vault_path)}")
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    if preview_only:
        print(f"\nPreview completed. Found {examples_shown} examples.")
        print("Run with 'python3 fix_image_links.py --fix' to apply changes.")
    else:
        print("\nFix completed!")
        print(f"Files modified: {files_modified}")
        print(f"Total links fixed: {total_fixes}")

if __name__ == "__main__":
    import sys
    
    # Use the correct path for WSL
    vault_path = "/mnt/c/Users/daanquin/Obsidian/new"
    
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        fix_obsidian_image_links(vault_path, preview_only=False)
    else:
        fix_obsidian_image_links(vault_path, preview_only=True)
