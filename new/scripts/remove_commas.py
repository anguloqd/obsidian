#!/usr/bin/env python3
"""
Script to remove commas from files/folders and update markdown references.
Uses the general markdown_reference_updater module.
"""

import os
import shutil
from pathlib import Path
from markdown_reference_updater import MarkdownReferenceUpdater

def remove_commas(name: str) -> str:
    """
    Remove commas from a filename/foldername.
    Examples: 
    - 'file, test.md' -> 'file test.md'
    - 'folder, name' -> 'folder name'
    - 'data, analysis, results.csv' -> 'data analysis results.csv'
    """
    return name.replace(',', '')

def get_paths_with_commas(root_dir):
    """Get all file and directory paths that contain commas."""
    paths_with_commas = []
    
    for root, dirs, files in os.walk(root_dir):
        # Add files with commas
        for file in files:
            if file not in ['remove_commas.py', 'markdown_reference_updater.py']:
                if ',' in file:
                    paths_with_commas.append(Path(root) / file)
        
        # Add directories with commas
        for dir_name in dirs:
            if ',' in dir_name:
                paths_with_commas.append(Path(root) / dir_name)
    
    # Sort by depth (deepest first) so we rename children before parents
    paths_with_commas.sort(key=lambda p: len(p.parts), reverse=True)
    return paths_with_commas

def rename_files_and_folders_remove_commas(paths_to_rename):
    """Rename files and folders to remove commas."""
    renamed_count = 0
    
    for old_path in paths_to_rename:
        old_name = old_path.name
        new_name = remove_commas(old_name)
        new_path = old_path.parent / new_name
        
        try:
            if old_path.exists():
                # Create parent directories if they don't exist
                new_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Rename the file/folder
                shutil.move(str(old_path), str(new_path))
                print(f"Renamed: {old_name} -> {new_name}")
                renamed_count += 1
        except Exception as e:
            print(f"Error renaming {old_path} to {new_path}: {e}")
    
    return renamed_count

def main():
    """Main function to remove commas from files/folders and update markdown references."""
    root_dir = Path(".")
    
    print("Starting comma removal process...")
    print(f"Root directory: {root_dir}")
    
    # Get all paths with commas
    print("Scanning for files and folders with commas...")
    paths_with_commas = get_paths_with_commas(root_dir)
    print(f"Found {len(paths_with_commas)} items with commas")
    
    if not paths_with_commas:
        print("No files or folders with commas found!")
        # Still check if we need to update markdown references
        print("Checking if markdown references need updating...")
        updater = MarkdownReferenceUpdater(remove_commas)
        updated, total = updater.update_all_markdown_files(root_dir)
        print(f"Updated references in {updated} out of {total} markdown files")
        return
    
    # Show preview
    print("\nPreview of changes:")
    for i, old_path in enumerate(paths_with_commas[:10]):
        old_name = old_path.name
        new_name = remove_commas(old_name)
        print(f"  {old_name} -> {new_name}")
    if len(paths_with_commas) > 10:
        print(f"  ... and {len(paths_with_commas) - 10} more")
    
    # Confirm with user
    response = input("\nProceed with removing commas? (y/N): ")
    if response.lower() != 'y':
        print("Comma removal cancelled.")
        return
    
    # Rename files and folders
    print("\nRenaming files and folders...")
    renamed_count = rename_files_and_folders_remove_commas(paths_with_commas)
    
    # Update markdown references using the general module
    print("\nUpdating markdown file references...")
    updater = MarkdownReferenceUpdater(remove_commas)
    updated_files, total_md_files = updater.update_all_markdown_files(root_dir)
    
    print("\nComma removal complete!")
    print(f"- Renamed {renamed_count} files and folders")
    print(f"- Updated references in {updated_files} out of {total_md_files} markdown files")

if __name__ == "__main__":
    main()
