
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def iterative_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    stack = []
    
    stack.append((0, len(arr) - 1))
    
    print(f"Initial array: {arr}")
    
    while stack:
        low, high = stack.pop()
        
        print(f"\nSorting subarray from index {low} to {high}: {arr[low:high+1]}")
        
        pi = partition(arr, low, high)
        print(f"Pivot index: {pi}, Current array: {arr}")
        
        if low < pi - 1:
            stack.append((low, pi - 1))
        
        if pi + 1 < high:
            stack.append((pi + 1, high))
    
    return arr

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

print(f"\nSorting array using iterative Quicksort...")
sorted_arr = iterative_quicksort(arr)

print(f"\nFinal sorted array: {sorted_arr}")
