import random
lst = [random.randint(1, 20) for i in range(10)]
print(lst)
for i in lst:
    if lst.count(i) > 1:
        print(i)