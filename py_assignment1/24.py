# Question 24: Find first occurrence of alphanumeric with consecutive repetitions using Group(s)

import re

def find_first_consecutive_char(text):
    # Pattern: Find any alphanumeric character repeated consecutively
    pattern = r'([a-zA-Z0-9])\1+'
    
    match = re.search(pattern, text)
    
    if match:
        print(f"Pattern found!")
        print(f"\nUsing group() methods:")
        print(f"  match.group() = '{match.group()}' (entire match)")
        print(f"  match.group(0) = '{match.group(0)}' (same as group())")
        print(f"  match.group(1) = '{match.group(1)}' (captured character from Group 1)")
        
        print(f"\nUsing groups() method:")
        print(f"  match.groups() = {match.groups()} (tuple of all captured groups)")
        
        print(f"\nUsing groupdict() method:")
        print(f"  match.groupdict() = {match.groupdict()} (named groups as dict)")
        
        print(f"\nMatch details:")
        print(f"  Position: {match.span()}")
        print(f"  Character '{match.group(1)}' repeats {len(match.group())} times")
        
        return match.group(1), match.group()
    else:
        print("No consecutive alphanumeric character found!")
        return None, None

# Main program
print("=== Find First Consecutive Character with Regex Groups ===\n")

test_cases = [
    "aabbcc",
    "The quick brown fox",
    "xyz112233",
    "hello world",
    "AABBCCdd",
    "Mississippi",
    "no_consecutive_here"
]

print("Testing with predefined strings:")
for text in test_cases:
    print(f"\nInput: '{text}'")
    char, match = find_first_consecutive_char(text)
    if char:
        print(f"First consecutive character: '{char}'")
    print()

print("\n--- Test with user input ---")
user_text = input("Enter a string to find consecutive characters: ")
char, match = find_first_consecutive_char(user_text)
if char:
    print(f"\nResult: First character with consecutive repetition is '{char}' appearing as '{match}'")
else:
    print(f"\nResult: No consecutive alphanumeric characters found")
