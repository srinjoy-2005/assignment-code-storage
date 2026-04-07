def get_sorted_chars(word):
    return ''.join(sorted(word))

def find_largest_anagram_group(words):
    anagram_groups = {}
    
    for word in words:
        key = get_sorted_chars(word)
        
        if key not in anagram_groups:
            anagram_groups[key] = []
        
        anagram_groups[key].append(word)
    
    # Find the group with maximum size
    if not anagram_groups:
        return 0
    
    max_group_key = max(anagram_groups.keys(), key=lambda k: len(anagram_groups[k]))
    max_group = anagram_groups[max_group_key]
    
    return len(max_group), max_group, anagram_groups

n = int(input("Enter the number of words: "))
words = []

for i in range(n):
    word = input(f"Enter word {i+1}: ").lower()
    words.append(word)

size, largest_group, all_groups = find_largest_anagram_group(words)

print(f"\nAll anagram groups:")
for key, group in all_groups.items():
    print(f"  {group} (size: {len(group)})")

print(f"\nLargest anagram subset: {largest_group}")
print(f"Size of largest anagram subset: {size}")
