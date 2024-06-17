fuck=int(input("Введите число: "))
from functools import reduce

fuci=[fuck]
while True:
    fuck -= 1
    fuci.append(fuck)
    if fuck==1:
        break
result = reduce(lambda x, y: x * y, fuci)
print(result)
