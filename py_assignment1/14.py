class priority_queue:
    def __init__(self, priority_function) -> None:
        self.arr = []
        self.priority = priority_function

    def _bubble_up(self):
        curr_idx = len(self.arr) - 1
        while curr_idx > 0:
            parent_idx = (curr_idx - 1) // 2
            # Max-Heap logic: if child priority > parent priority, swap
            if self.priority(self.arr[curr_idx]) > self.priority(self.arr[parent_idx]):
                self.arr[curr_idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[curr_idx]
                curr_idx = parent_idx
            else:
                break

    def _trickle_down(self):
        curr_idx = 0
        n = len(self.arr)

        while True:
            left = 2 * curr_idx + 1
            right = 2 * curr_idx + 2
            swap_idx = curr_idx

            # Check if left child has higher priority
            if left < n and self.priority(self.arr[left]) > self.priority(self.arr[swap_idx]):
                swap_idx = left
            
            # Check if right child has higher priority than current (or left)
            if right < n and self.priority(self.arr[right]) > self.priority(self.arr[swap_idx]):
                swap_idx = right

            if swap_idx == curr_idx:
                break

            self.arr[curr_idx], self.arr[swap_idx] = self.arr[swap_idx], self.arr[curr_idx]
            curr_idx = swap_idx

    def add(self, val):
        self.arr.append(val)
        self._bubble_up()

    def pop(self):
        if not self.arr:
            return None
        
        # 1. Grab the top (highest priority)
        root_val = self.arr[0]
        
        # 2. Move the last element to the top
        last_val = self.arr.pop()
        
        if self.arr: # Only re-insert and trickle if the list wasn't empty
            self.arr[0] = last_val
            self._trickle_down()
            
        return root_val

if __name__ == "__main__":
    pq_max = priority_queue(lambda x: x)
    pq_max.add(5)
    pq_max.add(1)
    pq_max.add(10)
    
    print("Testing Max-Heap...")
    assert pq_max.pop() == 10
    assert pq_max.pop() == 5
    assert pq_max.pop() == 1
    print("Max-Heap passed!")

    pq_min = priority_queue(lambda x: -x)
    pq_min.add(5)
    pq_min.add(1)
    pq_min.add(3)

    print("\nTesting Min-Heap...")
    assert pq_min.pop() == 1
    assert pq_min.pop() == 3
    assert pq_min.pop() == 5
    print("Min-Heap passed!")