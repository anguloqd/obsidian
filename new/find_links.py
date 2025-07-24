#!/usr/bin/env python3
import os
import glob

def find_problematic_links():
    vault_path = r"/mnt/c/Users/daanquin/Obsidian/new"
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    
    print(f"Found {len(md_files)} markdown files")
    print("Looking for image links with hashes...")
    count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if '![' in line and '](' in line:
                    # Check if line has 32-character hex pattern
                    import re
                    if re.search(r'[a-f0-9]{32}', line):
                        print(f"\nFile: {md_file}")
                        print(f"Line {i+1}: {line}")
                        count += 1
                        if count >= 10:  # Limit output
                            print(f"Found {count} problematic links, stopping here.")
                            return
        except Exception:
            continue
    
    print(f"Finished. Total problematic links found: {count}")

if __name__ == "__main__":
    find_problematic_links()
