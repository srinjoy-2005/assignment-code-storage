from collections import Counter
import re
import sys

# Please use python vesion >= 3.7 as the program uses f-strings, and makes uses of the fact that dictionaries preserve 
# insertion order

ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def number_to_words(n):
    if n == 0:
        return "Zero"
    
    words = []
    
    # Handle hundreds
    if n >= 100:
        words.append(ones[n // 100])
        words.append("Hundred")
        n = n % 100
    
    # Handle tens and ones
    if n >= 20:
        words.append(tens[n // 10])
        n = n % 10
        if n > 0:
            words.append(ones[n])
    elif n > 0:
        words.append(ones[n])
    
    return " ".join(words)

# if alphanumeric characters present in number to word print them sep... then print out the extracted number from words
# convert date(ddmmyyyy) to date format: 21st october, year

dict_of_months = {"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,
                  "september":30,"october":31,"november":30,"december":31
}

def year2word(year):
    upper = year // 100
    lower = year % 100
    
    def two_digits_to_words(n):
        if n < 20:
            return ones[n]
        else:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

    word_upper = two_digits_to_words(upper)
    if upper > 19:
        word_upper = f"{two_digits_to_words(int(upper//10))} thousand"
    word_lower = two_digits_to_words(lower)

    if lower == 0:
        return f"{word_upper} Hundred"
    
    return f"{word_upper} {word_lower}"

def num2word(x):
    if x >= 1e9:
        print("Number is too big for conversion!")
    elif x == 0:
        print("Zero")
    else:
        labels = ["Million", "Thousand", ""]
        
        m = x // 1000000
        t = (x // 1000) % 1000
        u = x % 1000
        
        blocks = [m, t, u]
        result = []

        for i in range(len(blocks)):
            if blocks[i] > 0:
                # Convert number to words
                words = number_to_words(blocks[i])
                result.append(words)
                if labels[i]:
                    result.append(labels[i])

        return (" ".join(result))

def process_file_for_num(file_path):
    try:
        with open(file_path, 'r') as f:
            arr = f.read().splitlines()

        for num in arr:
            non_digits = re.findall(r'\D', num)
            if non_digits:
                print(f"Non-digit characters found: {' '.join(non_digits)}")

            clean_content = re.sub(r'\D', '', num)
            print(f"Cleaned numeric string: {clean_content}")
            # using the funtion from the un-modified version
            word = num2word(int(clean_content))
            print(f"The number in words is: {word}")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    # Make sure of appropriate inputs within the file
    if len(sys.argv) < 2:
        print("Insufficient Arguements provided!")
        print("Please provide the path of the file along with the terminal command")
        sys.exit()
    if len(sys.argv) > 2:
        print("Too many arguements provided")
    
    print("Please enter 1 for date to words utility and any other value for numbers to words: ")
    
    choice = int(input("Enter utility: "))
    if choice == 1:
        file_path = sys.argv[1]
        with open(file_path,"r") as f:
            content = f.read()
        arr = content.splitlines()
        
        # Date in (DD/MM/YYYY) or (DD.MM.YYYY)

        for y in arr:
            if "/" in y:
                sep = '/'
            elif "." in y:
                sep = "."
            arr = y.strip().split(sep)
            day = int(arr[0])
            month_idx = int(arr[1])
            if month_idx > 12:
                print("Date is Invalid")
                sys.exit()

            year_val = int(arr[2])
            
            month_names = list(dict_of_months.keys())
            month_name = month_names[month_idx - 1]
            
            if day > dict_of_months[month_name]:
                print("Date is invalid")
                sys.exit()
            month_name = month_name.capitalize()
            suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
            print(f"{day}{suffix} {month_name}, {year2word(year_val)}")
        
    else:
        # This handles the 'file' or any other input
        file_path = sys.argv[1]
        process_file_for_num(file_path)
