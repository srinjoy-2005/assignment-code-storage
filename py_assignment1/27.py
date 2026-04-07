def snake_to_pascal(var_name:str):
    word_list = var_name.split('_')
    return "".join(word.capitalize() for word in word_list)

def snake_to_camel(var_name:str):
    word_list = var_name.split('_')
    return word_list[0].lower() + "".join(word.capitalize() for word in word_list[1:])

def snake_to_kebab(var_name:str):
    return var_name.replace("_","-")

# Main program
snake_case_input = input("Enter a snake_case string: ")

pascal = snake_to_pascal(snake_case_input)
camel = snake_to_camel(snake_case_input)
kebab = snake_to_kebab(snake_case_input)

print(f"\nOriginal (snake_case): {snake_case_input}")
print(f"PascalCase: {pascal}")
print(f"camelCase: {camel}")
print(f"kebab-case: {kebab}")
