#!/usr/bin/env python3
import os
import re

def fix_specific_files():
    vault_path = "/mnt/c/Users/daanquin/Obsidian/new"
    
    # Known files with issues
    problem_files = [
        "./uga/l3/s5/info/S5 info progra objets avancée et structures de do/04 généricité.md",
        "./uga/l3/s5/math/S5 math complé maths 1/03 équations différentielles.md", 
        "./uga/l3/s6/math/S6 math stats mathématiques 3/05 tests non paramétriques.md"
    ]
    
    pattern = r'(!\[.*?\]\([^)]*?)(%20[a-f0-9]{32})(\/[^)]*?\))'
    
    for rel_file in problem_files:
        full_path = os.path.join(vault_path, rel_file.lstrip('./'))
        print(f"\nProcessing: {rel_file}")
        
        try:
            # Read the file
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find matches
            matches = list(re.finditer(pattern, content))
            
            if matches:
                print(f"Found {len(matches)} problematic links:")
                for i, match in enumerate(matches):
                    original = match.group(0)
                    fixed = re.sub(pattern, r'\1\3', original)
                    print(f"  {i+1}. Before: {original}")
                    print(f"     After:  {fixed}")
                
                # Ask for confirmation
                response = input(f"\nFix {len(matches)} links in this file? (y/N): ")
                if response.lower() == 'y':
                    # Apply fixes
                    new_content = re.sub(pattern, r'\1\3', content)
                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✓ Fixed {len(matches)} links in {os.path.basename(full_path)}")
                else:
                    print("Skipped.")
            else:
                print("No problematic links found in this file.")
                
        except Exception as e:
            print(f"Error processing {full_path}: {e}")

if __name__ == "__main__":
    fix_specific_files()
