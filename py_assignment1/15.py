from heapq import nlargest,nsmallest

data = [12, 3, 45, 7, 23, 9, 31]
N = 3

largest_items = nlargest(N, data)
smallest_items = nsmallest(N,data)
print(f"largest items: {largest_items}")
print(f"smallest items: {smallest_items}")