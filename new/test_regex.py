#!/usr/bin/env python3
import re

# Test the regex pattern with known content from grep results
test_content = """![Untitled](new/uga/l3/s5/math/S5%20math%20complé%20maths%201/03%20équations%20différentielles%20c7c62f76a0064b409316869b31060490/Untitled.png)"""

patterns = [
    r'(!\[.*?\]\([^)]*?)(%20[a-f0-9]{32})(\/[^)]*?\))',
    r'(!\[.*?\]\([^)]*?)\s([a-f0-9]{32})(\/[^)]*?\))',
    r'(!\[.*?\]\([^)]*?) ([a-f0-9]{32})(\/[^)]*?\))',
    r'!\[.*?\]\([^)]*?[a-f0-9]{32}[^)]*?\)',
    r'!\[.*?\]\([^)]*?%20[a-f0-9]{32}[^)]*?\)',
]

print("Testing regex patterns on:")
print(repr(test_content))
print()

for i, pattern in enumerate(patterns):
    print(f"Pattern {i+1}: {pattern}")
    matches = re.findall(pattern, test_content)
    if matches:
        print(f"  Matches: {matches}")
    else:
        print("  No matches")
    print()

# Also test simpler search
if re.search(r'[a-f0-9]{32}', test_content):
    print("Found 32-char hex pattern in content")
else:
    print("No 32-char hex pattern found")
