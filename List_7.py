import random
lst = [random.randint(1, 20) for i in range(10)]
a = lst.index(max(lst))
b = lst.index(min(lst))
print(lst)
lst[a] , lst[b] = lst[b] , lst[a]
print(lst)