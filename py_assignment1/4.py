import re

def get_valid_phone_numbers(num_arr):
    pattern = r"^[6-9]\d{9}"
    valid_phone_num = []
    for nums in num_arr:
        if re.match(pattern,nums):
            valid_phone_num.append(nums)
    return valid_phone_num


if __name__ == "__main__":
    x = input("")
    nums = []
    for _ in range(int(x)):
        num = input("")
        nums.append(num)
    valid_nums = get_valid_phone_numbers(nums)
    print(f"The valid phone nums are: {valid_nums}")
