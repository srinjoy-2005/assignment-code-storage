from collections import Counter

def get_largest_set_of_anagrams(string:str):
    anagram_dict = {}
    for word in string.split():
        letters = ''.join(sorted(word))
        anagram_dict.setdefault(letters,[]).append(word)

    largest_set_of_anagrams = max(anagram_dict.values(),key = len)
    return largest_set_of_anagrams

if __name__ == "__main__":
    test_words = [
    "listen", "silent", "enlist", "tinsel", "inlets",   # large anagram group
    "rat", "tar", "art",                                # smaller group
    "evil", "vile", "veil", "live",                     # another group
    "stone", "tones", "onset", "notes",                 # medium group
    "loop", "pool", "polo", "lopo",                     # group of 4
    "python", "typhon",                                 # pair
    "dusty", "study",                                   # pair
    "angel", "glean", "angle",                          # group of 3
    "random", "words", "here"                           # no anagrams
]
    
    print(get_largest_set_of_anagrams(" ".join(test_words)))
