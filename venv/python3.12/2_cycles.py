#Дана пустая строка.
#Заполните с помощью цикла четными числами от 1 до 20.
empty_string=''

for num in range(2, 21, 2):
    empty_string += str(num) + ', '
print(empty_string)
