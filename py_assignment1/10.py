import time

def geometric_progression(num,a,b):
    val = a
    for idx in range(num):
        if val * b > 1e5:
            return 
        yield val
        val = val * b

if __name__ == "__main__":
    start_time = time.perf_counter()
    for val in (geometric_progression(100,1,9)):
        print(val)
    end_time = time.perf_counter()

    print(f"Total time taken: {end_time - start_time}ms")