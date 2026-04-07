def main1():
    return list(filter(lambda x: x % 5 == 0,range(1,51)))

def main2():
    return [x for x in range(1,51) if (lambda y: y % 5 == 0)(x)]

if __name__ == "__main__":
    print(f"Multiples of five using list_func and filter: {main1()}")
    print(f"Multiples of five using list comprehension: {main2()}")