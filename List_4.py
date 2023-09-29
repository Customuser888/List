import random
lst = [random.randint(1, 20) for i in range(10)]
print(lst)
a = 0
b = 1
for i in lst:
    a += i
    b *= i

print(a, b)