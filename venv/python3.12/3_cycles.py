# Выведите с помощью цикла
# столбец нечетных чисел от 100 до 1

for num in range(100, 1, -1):
    if num%2==0:
        continue
    print(num)

    print("Hello")

# ________________
# for num in range(100, 0, -1):
#     if num % 2 != 0:
#         print(num)
