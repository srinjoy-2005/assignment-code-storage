import re
import sys

def extract_hex_colors(css_code):
    pattern = r'#[0-9a-fA-F]{3,6}'
    
    matches = re.findall(pattern, css_code)
    
    return matches

if __name__ == "__main__":
    file_name = sys.argv[1]
    print(f"Reading css code from {file_name}")
    with open(file_name,"r") as f:
        css_code = f.read()

    # Extract hex colors
    hex_colors = extract_hex_colors(css_code)

    print(f"\nExtracted Hex Colors:")
    if hex_colors:
        for i, color in enumerate(hex_colors, 1):
            print(color)
    else:
        print("No valid hex color codes found")

    print(f"\nTotal unique colors: {len(set(hex_colors))}")
    print(f"Total occurrences: {len(hex_colors)}")
