import re
def is_valid_roman_numeral(s):
    # Pattern for valid Roman numerals 1-3999
    # M{0,3} = 0 to 3 M's (0, 1000, 2000, 3000)
    # (CM|CD|D?C{0,3}) = 900, 400, or 0-800
    # (XC|XL|L?X{0,3}) = 90, 40, or 0-80
    # (IX|IV|V?I{0,3}) = 9, 4, or 0-8
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    
    if re.match(pattern, s):
        return True
    else:
        return False

test_cases = ["IV", "IX", "LVIII", "MCMXCIV", "MMMCMXCIX", "IIII", "VV", "IC", "IM", ""]

for roman in test_cases:
    if roman == "":
        print(f"'{roman}' (empty): {is_valid_roman_numeral(roman)}")
    else:
        print(f"'{roman}': {is_valid_roman_numeral(roman)}")

print("\nTest with user input")
user_input = input("Enter a Roman numeral to validate: ").strip()

if is_valid_roman_numeral(user_input):
    print(f"True - '{user_input}' is a valid Roman numeral")
else:
    print(f"False - '{user_input}' is NOT a valid Roman numeral")
