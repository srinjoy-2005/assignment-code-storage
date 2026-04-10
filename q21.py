import re

# todo: extend to billio(1e9)


ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]


def two_digit_to_words(n):
    if n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    else:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")


def three_digit_to_words(n):
    if n < 100:
        return two_digit_to_words(n)
    else:
        return (ones[n // 100] + " hundred" +
                (" and " + two_digit_to_words(n % 100) if n % 100 != 0 else ""))


def year_to_words(n):
    first = n // 100
    last = n % 100

    result = two_digit_to_words(first) + " hundred"
    if last != 0:
        result += " and " + two_digit_to_words(last)

    return result


def number_to_words(n):
    if 1000 <= n <= 9999:
        return year_to_words(n)
    elif n < 1000:
        return three_digit_to_words(n)
    else:
        return str(n) 


def process_file(filename):
    with open(filename, "r") as f:
        text = f.read()

    # extract numbers
    numbers = re.findall(r"\b\d+\b", text)

    result = {}
    for num in numbers:
        n = int(num)
        result[num] = number_to_words(n)

    return result


if __name__ == "__main__":
    filename = "input.txt"

    mapping = process_file(filename)

    print("Extracted Numbers and their Word Forms:\n")
    for num, word in mapping.items():
        print(f"{num} → {word}")