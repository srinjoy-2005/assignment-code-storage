class Fibonacci_numbers:
    def __init__(self):
        self.idx = 0
        self.cache = {1:1,2:1}

    def __iter__(self):
        return self
    
    def __next__(self):
        self.idx += 1
        num = self.fib(self.idx)
        return num
        
    def fib(self,idx):
        if idx in self.cache.keys():
            return self.cache[idx]
        else: 
            val = self.fib(idx-1) + self.fib(idx-2)
            self.cache[idx] = val
            return val
        
        
def main():
    fib_num = Fibonacci_numbers()
    count = 9
    while count > 0:
        print(next(fib_num))
        count -= 1

if __name__ == "__main__":
    main()