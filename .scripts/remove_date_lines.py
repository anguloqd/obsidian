#!/usr/bin/env python3
"""
Script to clean up whitespace issues in Obsidian markdown files.
Removes excessive empty lines that were left after removing date metadata lines.
"""

import os
from pathlib import Path

def remove_date_lines_from_file(file_path):
    """
    Remove date lines from a single markdown file and clean up extra newlines.
    Returns True if the file was modified, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original_line_count = len(lines)
        
        # Filter out lines that start with "Date de création:" or "Modifié:"
        filtered_lines = []
        for line in lines:
            stripped_line = line.strip()
            if not (stripped_line.startswith("Date de création:") or 
                   stripped_line.startswith("Modifié:")):
                filtered_lines.append(line)
        
        # Clean up excessive empty lines at the beginning (after title)
        # Keep only one empty line after the title
        if len(filtered_lines) > 1:
            cleaned_lines = [filtered_lines[0]]  # Keep the title line
            
            # Skip consecutive empty lines after title, keep only one
            i = 1
            while i < len(filtered_lines) and filtered_lines[i].strip() == "":
                i += 1
            
            # Add one empty line if we had any
            if i > 1:
                cleaned_lines.append("\n")
            
            # Add the rest of the content
            cleaned_lines.extend(filtered_lines[i:])
            filtered_lines = cleaned_lines
        
        # If lines were removed, write the file back
        if len(filtered_lines) != original_line_count:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(filtered_lines)
            
            removed_count = original_line_count - len(filtered_lines)
            print(f"✓ {file_path.name}: Removed {removed_count} line(s) and cleaned whitespace")
            return True
        
        return False
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def find_markdown_files(root_dir):
    """Find all markdown files in the directory tree."""
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    return md_files

def preview_files_with_whitespace_issues(root_dir, max_preview=10):
    """Preview files that have excessive empty lines after the title."""
    md_files = find_markdown_files(root_dir)
    files_with_issues = []
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # Check for multiple consecutive empty lines after the title
            if len(lines) > 3:
                # Look for pattern: title, empty line, empty line, content
                if (lines[0].strip().startswith('#') and 
                    lines[1].strip() == "" and 
                    lines[2].strip() == ""):
                    files_with_issues.append(file_path)
                    
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
    
    print(f"\nFound {len(files_with_issues)} files with excessive whitespace:")
    for i, file_path in enumerate(files_with_issues[:max_preview]):
        rel_path = file_path.relative_to(root_dir)
        print(f"  {rel_path}")
    
    if len(files_with_issues) > max_preview:
        print(f"  ... and {len(files_with_issues) - max_preview} more files")
    
    return files_with_issues

def main():
    """Main function to clean up whitespace issues in markdown files."""
    root_dir = Path(".")
    
    print("Markdown Whitespace Cleanup Tool for Obsidian Vault")
    print("=" * 55)
    print(f"Scanning directory: {root_dir.absolute()}")
    
    # Preview files that will be affected
    files_with_issues = preview_files_with_whitespace_issues(root_dir)
    
    if not files_with_issues:
        print("\n✓ No files found with whitespace issues!")
        return
    
    # Confirm with user
    print(f"\nThis will clean up excessive empty lines in {len(files_with_issues)} files.")
    response = input("Proceed with cleaning whitespace? (y/N): ")
    if response.lower() != 'y':
        print("Operation cancelled.")
        return
    
    # Process all files
    print("\nProcessing files...")
    modified_count = 0
    
    for file_path in files_with_issues:
        if remove_date_lines_from_file(file_path):
            modified_count += 1
    
    print("\n✓ Whitespace cleanup complete!")
    print(f"  - Modified {modified_count} out of {len(files_with_issues)} files")
    print(f"  - Total markdown files scanned: {len(find_markdown_files(root_dir))}")

if __name__ == "__main__":
    main()
