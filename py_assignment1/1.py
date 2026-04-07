import sys

def get_primes(max_limit):
    arr = {i: True for i in range(2, max_limit+1)}
    prime_num = []
    for i in range(2,max_limit + 1):
        if arr[i] is True:
            prime_num.append(i)
            num = i
            while num <= max_limit:
                arr[num] = False
                num += i

    return prime_num


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Excess Arguments Provided")
        sys.exit()
    elif len(sys.argv) < 2:
        print("Insufficeint arguements Provided")
        sys.exit()

    max_lim = int(sys.argv[1])
    prime_num = get_primes(max_lim)
    print(prime_num)

