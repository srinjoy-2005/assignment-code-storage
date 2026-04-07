from collections import Counter
import re

class MyString:
    def __init__(self, string: str) -> None:
        self.string = string

    def _get_rep_words(self):
        cleaned_string = re.sub(r'[^\w\s]', '', self.string.lower())
        word_arr = cleaned_string.split()
        rep_arr = Counter(word_arr)
        return rep_arr

    def __len__(self):
        char_length = len(self.string)
        print(f"String length: {char_length}")
        rep_arr = self._get_rep_words()
        repeated = {word: len(word) for word, count in rep_arr.items() if count > 1}

        most_common_words = rep_arr.most_common()

        if repeated:
            print("Repeated words with their lengths:", repeated)
        else:
            print("No repeated words found.")

        print("Most common words:", most_common_words)

        return char_length


if __name__ == "__main__":
    s = MyString("cool string which is pretty cool, don't you think?")
    print(len(s))