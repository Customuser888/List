import random
n = int(input('Введите n: '))
lst = [random.randint(1, 100 ) for i in range(n)] 
print(lst[::2])