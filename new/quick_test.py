#!/usr/bin/env python3
import os
import re
import glob

def quick_test():
    vault_path = "/mnt/c/Users/daanquin/Obsidian/new"
    
    print("Searching for markdown files...")
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    print(f"Found {len(md_files)} markdown files")
    
    if len(md_files) == 0:
        print("No markdown files found - checking path...")
        if os.path.exists(vault_path):
            print(f"Path exists: {vault_path}")
            # List some contents
            contents = os.listdir(vault_path)[:10]
            print(f"First 10 items: {contents}")
        else:
            print(f"Path does not exist: {vault_path}")
        return
    
    pattern = r'(!\[.*?\]\([^)]*?)(%20[a-f0-9]{32})(\/[^)]*?\))'
    found_count = 0
    
    # Check first 5 files only
    for i, md_file in enumerate(md_files[:5]):
        print(f"Checking file {i+1}: {os.path.basename(md_file)}")
        try:
            with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Quick check for hex patterns
            if re.search(r'[a-f0-9]{32}', content):
                print(f"  Found 32-char hex in {os.path.basename(md_file)}")
                matches = re.finditer(pattern, content)
                for match in matches:
                    print(f"  Match: {match.group(0)[:100]}...")
                    found_count += 1
                    if found_count >= 3:
                        return
        except Exception as e:
            print(f"  Error: {e}")
    
    print(f"Total matches found: {found_count}")

if __name__ == "__main__":
    quick_test()
