# Заполните множеств
# (не упорядочено по умолчанию)
# с помощью
# цикла первыми 10-ю буквами английского
# алфавита.

import string

alphabet = string.ascii_lowercase
my_set = set()
counter = 0

for letter in alphabet:
    my_set.add(letter)
    counter += 1
    if counter == 10:
        break

print(my_set)




