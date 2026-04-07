def number_to_words(n):
    if n == 0:
        return "Zero"
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
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

x = int(input("Enter the number: "))

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

    print(" ".join(result))

# if alphanumeric characters present print them... if any four digit year is present show them separately
# date format: 21st october