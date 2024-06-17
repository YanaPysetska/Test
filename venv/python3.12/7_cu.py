# Дана строка. С помощью цикла проверьте,
# есть ли в ней буква 'c'.

str='sdlfjdhfkgjhsdighdshkgcsdfa'
found = False  # Флаг для отслеживания наличия буквы 'c' в строке
for i in str:
    if i =='c':
        found = True  # Устанавливаем флаг, если символ 'c' найден
        break  # Прерываем цикл, так как буква 'c' уже найдена
if found:
    print('Yes')
else:
    print('No')
