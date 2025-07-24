#!/usr/bin/env python3
import os
import re
import glob

def debug_pattern_matching():
    vault_path = r"/mnt/c/Users/daanquin/Obsidian/new"
    
    # Find files containing the specific hash
    test_hash = "c7c62f76a0064b409316869b31060490"
    
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if test_hash in content:
                print(f"Found hash in: {md_file}")
                
                # Find lines containing the hash
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if test_hash in line:
                        print(f"Line {i+1}: {repr(line)}")
                        
                        # Try different patterns
                        patterns = [
                            r'(!\[.*?\]\([^)]*?)\s([a-f0-9]{32})(\/[^)]*?\))',
                            r'(!\[.*?\]\([^)]*?)%20([a-f0-9]{32})(\/[^)]*?\))',
                            r'(!\[.*?\]\([^)]*?) ([a-f0-9]{32})(\/[^)]*?\))',
                            r'!\[.*?\]\([^)]*?[a-f0-9]{32}[^)]*?\)',
                        ]
                        
                        for j, pattern in enumerate(patterns):
                            matches = re.finditer(pattern, line)
                            for match in matches:
                                print(f"Pattern {j+1} matched: {repr(match.group(0))}")
                break
        except Exception as e:
            continue

if __name__ == "__main__":
    debug_pattern_matching()
