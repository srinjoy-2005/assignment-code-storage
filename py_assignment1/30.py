def generate_series(n, k):
    result = []
    
    def go_down(current):
        result.append(current)
        print(f"Going down: {current}", end="")
        
        if current - k >= 0: 
            go_down(current - k)
        else:  
            go_up(current - k)
    
    def go_up(current):
        result.append(current)
        print(f"Going up: {current}", end="")
        
        if current + k <= n:
            go_up(current + k)
        else:
            print("done")
    
    go_down(n)
    return result


def helperGetNum(N, n, k, has_flipped, arr):
    if not has_flipped:
        n -= k
        arr.append(n)
        if n < 0: 
            has_flipped = True
        return helperGetNum(N, n, k, has_flipped, arr)
    else:
        n += k
        arr.append(n)
        if n == N:
            return arr
        else:
            return helperGetNum(N, n, k, has_flipped, arr)


def getNum(N, k):
    has_flipped = False
    arr = [N]
    helperGetNum(N, N, k, has_flipped, arr)
    return arr


def get_num_recursive(n, k):
    res = [n]
    
    if n > 0:
        inner_list = get_num_recursive(n - k, k)
        res = res + inner_list + [n]
        
    return res


# Main program
print("Number Series Generator\n")

n = int(input("Enter N: "))
k = int(input("Enter K: "))

print("\nChoose an algorithm:")
print("1. Nested functions (go_down/go_up)")
print("2. Helper function with flag")
print("3. Pure recursive approach")

choice = input("\nEnter your choice (1-3): ").strip()

print(f"\nGenerating series for N={n}, K={k}:")

if choice == "1":
    series = generate_series(n, k)
elif choice == "2":
    series = getNum(n, k)
elif choice == "3":
    series = get_num_recursive(n, k)
else:
    print("Invalid choice. Using method 1.")
    series = generate_series(n, k)

print(f"\nResulting series: {' '.join(map(str, series))}")