from collections import Counter
import re

class MyString:
    def __init__(self,raw_text:str,word_arr:list[str]) -> None:
        self.raw_text = raw_text
        self.word_arr = word_arr

    @classmethod
    def process_string(cls,raw_text):
        clean_text = re.sub(r'[^\w\s]', '', raw_text.lower())
        words = clean_text.strip().split()
        return cls(clean_text,words)
    
    def get_unique_words(self):
        unique_words = set(self.word_arr)
        return unique_words
    
    def get_palindromes(self):
        palindromes = []
        for word in self.word_arr:
            if word == word[::-1]:
                palindromes.append(word)

        return palindromes
    
if __name__ == "__main__":

    text = "Madam, I refer to the level of racecar driving in civic centers."

    # Use the Class Method to create the object
    analyzer = MyString.process_string(text)

    print(f"Unique Words: {analyzer.get_unique_words()}")
    print(f"Palindromes: {analyzer.get_palindromes()}")
    
