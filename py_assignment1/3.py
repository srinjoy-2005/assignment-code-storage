class OddNumbers:
    def __init__(self):
        self.num = -1
    def __next__(self):
        self.num += 2
        return self.num

num = OddNumbers()
print(next(num))
print(next(num))
print(next(num))

class EvenNumbers:
    def __init__(self):
        self.num = 0
    def __next__(self):
        self.num += 2
        return self.num

num = EvenNumbers()
print(next(num))
print(next(num))
print(next(num))


# class myvector:
#     def __init__(self):
#         pass
#     def __str__(self)-> str:
#         return "My vector"
# new = myvector()
# print(new)