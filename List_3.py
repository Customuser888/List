import random
lst = [random.randint(1, 100) for i in range(10)]
print(lst)
a = int(input())
if a in lst:
  print(lst.index(a))
else:
  print(-1)