#!/usr/bin/env python3
"""
Script to rename files/folders and update markdown references to remove accented characters.
Uses the general markdown_reference_updater module.
"""

import os
import shutil
import unicodedata
from pathlib import Path
from scripts.markdown_reference_updater import MarkdownReferenceUpdater

def remove_accents_from_name(name: str) -> str:
    """
    Remove accented characters from a filename/foldername.
    Examples: 
    - 'café' -> 'cafe'
    - 'résumé' -> 'resume'
    - 'naïve' -> 'naive'
    """
    # Normalize to NFD (decomposed form) and remove combining characters
    normalized = unicodedata.normalize('NFD', name)
    # Remove combining characters (accents)
    without_accents = ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')
    return without_accents

def get_all_paths_with_accents(root_dir):
    """Get all file and directory paths that contain accented characters."""
    all_paths = []
    
    for root, dirs, files in os.walk(root_dir):
        # Add files with accents
        for file in files:
            if file not in ['remove_accents.py', 'markdown_reference_updater.py']:
                original_name = file
                no_accent_name = remove_accents_from_name(original_name)
                if original_name != no_accent_name:
                    all_paths.append(Path(root) / file)
        
        # Add directories with accents
        for dir_name in dirs:
            original_name = dir_name
            no_accent_name = remove_accents_from_name(original_name)
            if original_name != no_accent_name:
                all_paths.append(Path(root) / dir_name)
    
    # Sort by depth (deepest first) so we rename children before parents
    all_paths.sort(key=lambda p: len(p.parts), reverse=True)
    return all_paths

def rename_files_and_folders_remove_accents(paths_to_rename):
    """Rename files and folders to remove accented characters."""
    renamed_count = 0
    
    for old_path in paths_to_rename:
        old_name = old_path.name
        new_name = remove_accents_from_name(old_name)
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
    """Main function to remove accents from files/folders and update markdown references."""
    root_dir = Path(".")
    
    print("Starting accent removal process...")
    print(f"Root directory: {root_dir}")
    
    # Get all paths with accented characters
    print("Scanning for files and folders with accented characters...")
    paths_with_accents = get_all_paths_with_accents(root_dir)
    print(f"Found {len(paths_with_accents)} items with accented characters")
    
    if not paths_with_accents:
        print("No files or folders with accented characters found!")
        # Still check if we need to update markdown references
        print("Checking if markdown references need updating...")
        updater = MarkdownReferenceUpdater(remove_accents_from_name)
        updated, total = updater.update_all_markdown_files(root_dir)
        print(f"Updated references in {updated} out of {total} markdown files")
        return
    
    # Show preview
    print("\nPreview of changes:")
    for i, old_path in enumerate(paths_with_accents[:10]):
        old_name = old_path.name
        new_name = remove_accents_from_name(old_name)
        print(f"  {old_name} -> {new_name}")
    if len(paths_with_accents) > 10:
        print(f"  ... and {len(paths_with_accents) - 10} more")
    
    # Confirm with user
    response = input("\nProceed with removing accents? (y/N): ")
    if response.lower() != 'y':
        print("Accent removal cancelled.")
        return
    
    # Rename files and folders
    print("\nRenaming files and folders...")
    renamed_count = rename_files_and_folders_remove_accents(paths_with_accents)
    
    # Update markdown references using the general module
    print("\nUpdating markdown file references...")
    updater = MarkdownReferenceUpdater(remove_accents_from_name)
    updated_files, total_md_files = updater.update_all_markdown_files(root_dir)
    
    print("\nAccent removal complete!")
    print(f"- Renamed {renamed_count} files and folders")
    print(f"- Updated references in {updated_files} out of {total_md_files} markdown files")

if __name__ == "__main__":
    main()
