import re

# Read dimensions
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

print(f"Matrix dimensions: {n} rows x {m} columns")

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(f"\nOriginal matrix (rows):")
for i, row in enumerate(matrix):
    print(f"  Row {i}: {row}")

# Decode by reading columns instead of rows
# zip(*matrix) transposes the matrix - it reads column by column
print(f"\nTransposing (reading column by column):")
decoded_string = ""
for col_idx, column in enumerate(zip(*matrix)):
    col_string = "".join(column)
    print(f"  Column {col_idx}: {col_string}")
    decoded_string += col_string

print(f"\nDecoded string (before cleaning): {decoded_string}")

# Replace any symbols/spaces between alphanumeric characters with a single space
# (?<=\w) = lookbehind for word character
# ([^\w]+) = capture one or more non-word characters
# (?=\w) = lookahead for word character
cleaned_script = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', decoded_string)

print(f"Final cleaned script: {cleaned_script}")