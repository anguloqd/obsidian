#!/usr/bin/env python3
"""
Verification script to check if the fixes were applied successfully.
"""

import os
import re

def verify_fixes(vault_path):
    """
    Check if any broken links remain in the vault.
    """
    
    pattern = r'%20[a-f0-9]{32}'
    total_files = 0
    files_with_remaining_issues = 0
    total_remaining_links = 0
    
    print("🔍 Verifying that all broken links have been fixed...")
    print("=" * 50)
    
    # Walk through all directories
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                total_files += 1
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, vault_path)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    
                    # Check for remaining hash patterns
                    matches = re.findall(pattern, content)
                    
                    if matches:
                        files_with_remaining_issues += 1
                        total_remaining_links += len(matches)
                        print(f"⚠️  {relative_path}: {len(matches)} remaining issues")
                
                except Exception as e:
                    print(f"❌ Error reading {relative_path}: {e}")
    
    # Final report
    print("\n" + "=" * 50)
    print("📊 VERIFICATION RESULTS:")
    print(f"   Total files checked: {total_files}")
    print(f"   Files with remaining issues: {files_with_remaining_issues}")
    print(f"   Total remaining broken links: {total_remaining_links}")
    
    if files_with_remaining_issues == 0:
        print("   ✅ SUCCESS: All broken links have been fixed!")
    else:
        print("   ⚠️  Some issues remain and need manual attention.")

if __name__ == "__main__":
    vault_path = "/mnt/c/Users/daanquin/Obsidian/new"
    verify_fixes(vault_path)
