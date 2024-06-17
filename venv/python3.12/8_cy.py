# Дан список с числами.
# Найдите среднее арифметическое
# его элементов.

my_list=[67, 23, 54, 89, 12, 45, 76, 34, 98, 21]
result_plus=0
for i in my_list:
    result_plus+=i

arifm=result_plus/len(my_list)
print(arifm)



