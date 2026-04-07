import re

def get_match(string:str):
    pattern = r"([a-zA-Z0-9])\1+"
    match_obj = re.search(pattern,string)
    if match_obj:
        return match_obj.group(),match_obj.group(1),match_obj.groups()
    else: return None
    
if __name__ == "__main__":
    cool_word = "hey"
    print(get_match(cool_word))