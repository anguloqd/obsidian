#!/usr/bin/env python3
"""
General-purpose module for updating markdown references based on transformation rules.
This module can be reused for any type of file/folder name transformation.
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote
from typing import Callable, Tuple

class MarkdownReferenceUpdater:
    """
    A class to update markdown file references based on custom transformation rules.
    """
    
    def __init__(self, transformation_rule: Callable[[str], str]):
        """
        Initialize the updater with a transformation rule.
        
        Args:
            transformation_rule: A function that takes a string (filename/path) and returns the transformed string
        """
        self.transformation_rule = transformation_rule
    
    def normalize_path(self, path_part: str) -> str:
        """
        Normalize a file path by applying the transformation rule to each part.
        
        Args:
            path_part: The path string to normalize
            
        Returns:
            The normalized path string
        """
        # Decode URL encoding if present (handles %20 for spaces, etc.)
        path_part = unquote(path_part)
        
        # Split path into parts and transform each part
        if path_part.startswith('new/'):
            # Convert absolute reference starting with 'new/'
            relative_path = path_part[4:]  # Remove 'new/' prefix
            parts = relative_path.split('/')
            new_parts = [self.transformation_rule(part) for part in parts]
            return 'new/' + '/'.join(new_parts)
        else:
            # Handle relative paths
            parts = path_part.split('/')
            new_parts = [self.transformation_rule(part) for part in parts]
            return '/'.join(new_parts)
    
    def update_file_references(self, file_path: Path) -> bool:
        """
        Update all references in a markdown file based on the transformation rule.
        
        Args:
            file_path: Path to the markdown file to update
            
        Returns:
            True if the file was modified, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Update image/attachment references like ![description](path/to/file.ext)
            def replace_attachment_ref(match):
                description = match.group(1)
                path_part = match.group(2)
                
                # Skip external URLs
                if path_part.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                    return match.group(0)
                
                new_path = self.normalize_path(path_part)
                return f'![{description}]({new_path})'
            
            content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_attachment_ref, content)
            
            # 2. Update wiki-style links [[Page Name]] or [[Page Name|Display Text]]
            def replace_wiki_link(match):
                link_content = match.group(1)
                if '|' in link_content:
                    link_target, display_text = link_content.split('|', 1)
                    # Only transform the target, keep display text as is
                    return f'[[{self.transformation_rule(link_target)}|{display_text}]]'
                else:
                    return f'[[{self.transformation_rule(link_content)}]]'
            
            content = re.sub(r'\[\[([^\]]+)\]\]', replace_wiki_link, content)
            
            # 3. Update regular markdown links [text](path) - for PDFs and other files
            def replace_md_link(match):
                text = match.group(1)
                path_part = match.group(2)
                
                # Skip external URLs
                if path_part.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                    return match.group(0)
                
                new_path = self.normalize_path(path_part)
                return f'[{text}]({new_path})'
            
            content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_md_link, content)
            
            # 4. Update Obsidian-style attachment links ![[filename.ext]]
            def replace_obsidian_attachment(match):
                filename = match.group(1)
                # Skip if it looks like an external reference
                if filename.startswith(('http://', 'https://')):
                    return match.group(0)
                return f'![[{self.transformation_rule(filename)}]]'
            
            content = re.sub(r'!\[\[([^\]]+)\]\]', replace_obsidian_attachment, content)
            
            # 5. Update any remaining file paths in the content
            def replace_bare_paths(match):
                full_match = match.group(0)
                path_part = match.group(1)
                
                # Skip if it's an external URL
                if path_part.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                    return full_match
                
                # Only process if it contains vault structure patterns
                if 'new/' in path_part or any(folder in path_part for folder in ['uga/', 'ensimag/', '_assets/']):
                    new_path = self.normalize_path(path_part)
                    return full_match.replace(path_part, new_path)
                
                return full_match
            
            # Pattern to catch remaining file paths
            content = re.sub(r'(\S*(?:new/|uga/|ensimag/|_assets/)\S*)', replace_bare_paths, content)
            
            # Only write if content changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
            
            return False
            
        except Exception as e:
            print(f"Error updating references in {file_path}: {e}")
            return False
    
    def update_all_markdown_files(self, root_dir: Path = None) -> Tuple[int, int]:
        """
        Update references in all markdown files in the given directory.
        
        Args:
            root_dir: Root directory to search for markdown files (defaults to current directory)
            
        Returns:
            Tuple of (updated_files_count, total_markdown_files_count)
        """
        if root_dir is None:
            root_dir = Path(".")
        
        updated_files = 0
        total_md_files = 0
        
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.md'):
                    total_md_files += 1
                    file_path = Path(root) / file
                    if self.update_file_references(file_path):
                        print(f"Updated references in: {file_path}")
                        updated_files += 1
        
        return updated_files, total_md_files


# Example transformation rules that can be used with the updater

def spaces_to_underscores_lowercase(name: str) -> str:
    """Transform spaces to underscores and convert to lowercase."""
    return name.replace(' ', '_').lower()

def remove_accents(name: str) -> str:
    """Remove accented characters and replace them with non-accented equivalents."""
    import unicodedata
    # Normalize to NFD (decomposed form) and remove combining characters
    normalized = unicodedata.normalize('NFD', name)
    # Remove combining characters (accents)
    without_accents = ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')
    return without_accents

def spaces_to_underscores_lowercase_no_accents(name: str) -> str:
    """Combine multiple transformations: spaces to underscores, lowercase, remove accents."""
    # First remove accents
    no_accents = remove_accents(name)
    # Then apply spaces to underscores and lowercase
    return spaces_to_underscores_lowercase(no_accents)


# Convenience function for quick use
def update_markdown_references_with_rule(transformation_rule: Callable[[str], str], 
                                       root_dir: Path = None) -> None:
    """
    Convenience function to update markdown references with a given transformation rule.
    
    Args:
        transformation_rule: Function to transform filenames/paths
        root_dir: Root directory to process (defaults to current directory)
    """
    updater = MarkdownReferenceUpdater(transformation_rule)
    updated, total = updater.update_all_markdown_files(root_dir)
    
    print("\nMarkdown reference update complete!")
    print(f"- Updated references in {updated} out of {total} markdown files")


if __name__ == "__main__":
    # Example usage
    print("This is a module for updating markdown references.")
    print("Import it and use it with your custom transformation rules.")
    print("\nExample usage:")
    print("from markdown_reference_updater import update_markdown_references_with_rule, remove_accents")
    print("update_markdown_references_with_rule(remove_accents)")
