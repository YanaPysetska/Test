import math
# num1 = 5
# num2 = 4
# # result=num1**num2
# result=pow(num1,num2)
# print(result)

# dct = {
# 	2: 4,
# 	3: 2,
# 	5: 4
# }
# for key, value in dct.items():
#     result=pow(key,value)
#     print(result)


# num = 16
# result = math.sqrt(num)
# print(result)

# lst = [2, 3, 4]
# res=0
# for i in lst:
#     res+=i
# result=math.sqrt(res)
# print(result)


# num = 16.456
# print(round(num))

# num = 21.167
# print(round(num,2))

# num = 3.348
# print(math.ceil(num))

# num = 18.565
# print(math.floor(num))

# num = 17
# result=math.sqrt(num)
# print(round(result,2))

# num = 17
# result = pow(num, 1/3)
# print(math.ceil(result))

# lst = [3.45, 1.54, 5.76]
# for i in lst:
#     print(math.ceil(i))


# lst1 = [1.514, 4.897, 2.657]
# lst2 = []
# for i in lst1:
#     lst2.append(math.floor(i))
# print(lst2)



# lst = [2, 4, 6, 8]
# print(max(lst))

# tlp = (-1, 2, -6, 3)
# print(min(tlp))

# dct = {
# 	'a': 2,
# 	'b': 4,
# 	'c': 5,
# 	'd': 1
# }
# print(max(dct.values()))

# num = 123456
# lst=[]
# for i in str(num):
#     lst.append(int(i))
# print(lst)
# print(max(lst))
# print(min(lst))
import random

# 175
# num1 = 10
# num2 = 20
# print(random.randrange(num1, num2))

# num1 = 5
# num2 = 30
# print(random.randint(num1, num2))

# num1 = 1.345
# num2 = 14.784
# num1 = -2
# num2 = 10
# num1 = 5
# num2 = 50
# num3 = 4
# print(random.randrange(num1, num2, num3))

# lst = [1, 2, 3, 4, 5]
# # print(random.choice(lst))
# # print(random.sample(lst, 3))

# lst = [1, 2, 3, 4, 5]
# random.shuffle(lst)
# print(lst)


# lst = [1, 1, 1, 2, 2, 3, 3, 4, 5]
# print(random.sample(lst, 3))


# tlp = (10, 6, 2, 4)
# chislo=random.sample(tlp,1)
# print(type(chislo))
# my_chislo=''.join(map(str,chislo))
# print(type(int(my_chislo)))


# import random
#
# lst = [1, 1, 1, 2, 2, 3, 3, 4, 5]

# # Удаляем дубликаты из списка
# unique_elements = list(set(lst))
#
# # Если уникальных элементов меньше или равно 3, выбираем все элементы
# if len(unique_elements) <= 3:
#     random_selection = unique_elements
# else:
#     # Иначе, случайным образом выбираем три уникальных элемента
#     random_selection = random.sample(unique_elements, 3)
#
# print(random_selection)



# num1 = -8
# num2 = -2
#
# print(abs(num1)+abs(num2))

# lst1 = [-3, 4, -1, 6]
# lst2 = []
#
# for i in lst1:
#     result=abs(i)
#     lst2.append(result)
# print(lst2)

# lst = [1, 2, 3, 4, 5]
# print(sum(lst))

# st = {2.3, 4, 7.8}
# print(math.sum(st))


# num1 = 2
# num2 = 15
# ran_ran=random.randint(num1, num2)
# print(ran_ran)
# print(math.factorial(ran_ran))


# lst = [1, 2, 3, 4, 5]
# print(sum(lst)/len(lst))

#178
# import math
# num1 = 5
# num2 = 3
# print(divmod(num1, num2))

# num = 4.8
# my_list=list(math.modf(num))
# print(my_list)

# txt = 'ABCDE'
# print(txt.lower())

# txt = 'abcde'
# print(txt.upper())

# txt = 'abcde'
# print(txt.capitalize())

# txt = 'word1 word2 word3'
# words = txt.split()
# for i in words:
#     print(i.capitalize())

# txt = 'ABC def'
# words = txt.split()
# for i in words:
#     break
# print(txt.swapcase())


# lst = ['ab', 'Cd', 'eF']
# for string in lst:
#     print(string.title())


# users_emails = {
#     "alice": "alice@example.com",
#     "bob": "bob@example.com",
#     "charlie": "charlie@example.com"
# }
# for i in users_emails.values():
#     print(i.casefold())

# txt = 'a.b.c.d'
# my_list=txt.rsplit('.',1)
# print(my_list)


# txt = 'ab%cd%'
# print(txt.partition('%'))

# txt = '2025-12-31'
# print(txt.rpartition('-'))


# lst = ['a', 'b', 'c', 'd']
# txt = ''.join(lst)
# print(txt)


# lst = ['2025', '31', '12']
# txt = '/'.join(lst)
# print(txt)

#
# lst = [1, 2, 3]
# string_result =''.join(map(str, lst))
# print(string_result)


# txt = 'a1bc11de'
# new_list=[]
# for i in txt:
#     if i=='1':
#         continue
#     else:
#         new_list.append(i)
# print(new_list)


# txt = ' abcde '
# print(txt.strip())
# print(txt.lstrip())
# print(txt.rstrip())


# txt = 'abc {}'
# num = 12
# print(txt.format(num))


# txt = ''
# num = 6
# print(txt.zfill(num))

# txt = 'abcde'
# print(txt.ljust(8, '1'))


# txt = '12345'
# print(txt.rjust(7, 'a'))

# txt = 'abcdef'
# print(txt.startswith( 'ac'))

# lst = ['12', '13', '14', '15', '90']
# for i in lst:
#     if i.startswith('1'):
#         print(i)
#     else:
#         print('No')


# num = 123456
# print(str(num).endswith('6'))


# txt = 'abcdef'
# print(txt.find('c'))

# txt = 'ab1cd1ef'
# print(txt.find('1', 3,7))


# txt = '123453637'
# print(txt.rindex('3'))


# num = 24536589
# print(str(num).count('5'))


# lst = ['abc', 'cde', 'cbb', 'aeb']
# for i in lst:
#     print(i.count('b'))


# txt = 'http1://code.mu'
# print(txt.replace('1', 's'))

# txt = 'a.bc.d.ef'
# print(txt.replace('.', ' '))

# txt = '2025.12.31'
# print(txt.rindex('2'))

# txt = 'Abcde'
# print(txt.istitle())


# lst = ['User1', 'User2', 'user3', 'User4']
# for i in lst:
#     print(i.istitle())

# txt = 'ABCDE'
# print(txt.isupper())


# txt = 'abcde'
# print(txt.islower())


# txt = 'abcde'
# print(txt.isalpha())


# txt = '12345'
# print(txt.isdigit())

# txt = 'Ⅷ'
# is_digit = txt.isdigit()
#
# print(is_digit)  # Вывод: True

# txt = '12345abc'
# print(txt.isalnum())
# txt = 'a1b2c3d '
# print(txt.isalnum())


# txt = ' '
# print(txt.isspace())


# lst = ['a', 'b', ' ', 'c', '']
# for i in lst:
#     print(i.isspace())


import datetime
# birthdate = datetime.date(1993, 8, 14)
# print(birthdate)
# print(birthdate.year)
# print(birthdate.day)
# print(birthdate.month)
#
# res = datetime.date.today()
# print(res)
# print(res.day)
# print(res.month)
# print(res.year)

# res = datetime.date.today()
# print(res.weekday())
# print(res.isoweekday())

# res = datetime.date(2026, 11, 2)
# print(res.weekday())
# print(res.isoweekday())



# start_time = datetime.datetime.strptime('01-12-2025 16:07:5',
# 	'%d-%m-%Y %H:%M:%S')
# end_time = datetime.datetime.strptime('31:12:2025 10:32:45',
# 	'%d:%m:%Y %H:%M:%S')
#
# res = end_time - start_time
# print(res)



import calendar
# res = datetime.date.today()
# res_2 = calendar.isleap(res.year)
# print(res_2)
# from datetime import datetime
# current_time = datetime.now().time()
# formatted_time = current_time.strftime("%H:%M:%S")
# print(formatted_time)

# res = datetime.date.today()
# res_2 = res.strftime('%d-%m-%Y')
# print(res_2)

# from datetime import datetime
# now = datetime.now()
# print(now)
# formatted_datetime = now.strftime("%H:%M:%S %Y/%m/%d:%A")
# print(formatted_datetime)


# import time
#
# res = time.time()
# print(res)
#
# dt = time.time()
# res = time.ctime(dt)
#
# print(res)
import time
# now = time.time()
# res = time.localtime(now)
#
# print(res)
# print(res.tm_hour)

# dt = 1602314100.0
# res = time.localtime(dt)
# print(res)

#
# now = time.time()
# res = time.gmtime(now)
#
# print(res)
# obj = time.localtime()
# print(obj)


# now = time.time()
# st_time = time.gmtime(now)
# res = time.mktime(st_time)
# print(res)

# from datetime import datetime
# time.sleep(2)
# current_time=datetime.now().time()
# print(current_time)

# lst = ['a', 'b', 'c', 'd']
# for i in lst:
#     print(i)
#     time.sleep(3)

# def my_func():
#     print('name ->Yana')
#     print('surname->Pysetska')
# my_func()

# def my_sum():
#     print(f'{3+6}')
# my_sum()


# def kvadrat(num1, num2):
#     print(num1*num2)
#
# kvadrat(3,5)

#
# def kvadrat(num1):
#     if num1%2==0:
#         print('четное')
#     else:
#         print('нечетное')
#
# kvadrat(4)



# def spisok(lis):
#     res=0
#     for i in lis:
#         res+=i**2
#     print(res)
#
# spisok([1,2,3])


# def par_chis(num1):
#     return num1**3
#
# res=par_chis(3)+par_chis(2)
# print(res)

#
# def func1(num1, num2, num3):
# 	return (num1 + num2) * num3
#
# res=func1(num1=1, num2=2, num3=2)
# print(res)


# def func1(text1, text2):
# 	return text1 + ' ' + text2
#
# res=func1(text1='hello', text2='Yana')
# print(res)

# def paramerty(num1,num2,num3):
#     return num1+num2+num3
#
# tst1 = 2
# tst2 = 4
# tst3 = 6
# res=paramerty(tst1,tst2,tst3)
# print(res)


# def func(lst):
# 	sum = 0
#
# 	for el in lst:
# 		sum += el
#
# 	return sum
#
# tst = [1, 3, 6]
#
# res=func(tst)
# print(res)



# def square(num):
# 	return num ** 2
#
# def cube(num):
# 	return num ** 3
#
# def add(num1, num2):
# 	return square(num1) ** cube(num2)
#
# res = add(2, 4)
# print(res)

# def vstroka(stroka):
#     if isinstance(stroka, str)==True:
#         return stroka.title()
# def hello_name(stroka):
#     return (f'hello  {vstroka(stroka)}')
#
# result=hello_name('Yana')
# print(result)

# num1 = 2
# num2 = 3
# def func(num1, num2):
#     pass
# res = func(num1, num2)
# print(res)

# tst1 = 'abc'
# tst2 = 'def'
#
# def func1(txt):
# 	return txt.upper()
#
# def func2(txt1, txt2):
#     pass
# res = func2(func1(tst1), tst2)
# print(res)

# def func(num1, num2):
#     '''function for multiply two numbers'''
#     return num1 * num2


# def student(student_name,student_surname,student_course):
#     return student_name.title(), student_surname.upper(), student_course
#
# res=student('Yana', 'Pusetska', 4)
# print(res)

# def square_square(a,b):
#     return a*b
#
# res=square_square(3, 2)
# print(res)

# def stroka_to_kortej(stroka):
#     return tuple(stroka)
#
# res=stroka_to_kortej('Yana')
# print(res)

# def proverka_chisel(num1, num2):
#     if num1>num2:
#         return('первое больше второго')
#     elif num2>num1:
#         return('второе большге первого')
#     else:
#         return ('числа равны')
#
# res=proverka_chisel(2,4)
# print(res)


# def type_perem(typething):
#     if isinstance(typething, int) or isinstance(typething, float):
#         return str(typething)
#     else:
#         return typething
#
# res=type_perem(1)
# print(res)
#
# res=type_perem('Yana')
# print(res)


# def even_numbers(num):
#     res=1
#     list_my=[]
#     while res<=num:
#         if res % 2 == 0:
#             list_my.append(res)
#         res += 1
#     print(list_my)
#
# even_numbers(6)



# def koetrj(users):
#     return tuple(users.items())
#
# users = {
#     "Alice": 25,
#     "Bob": 30,
#     "Charlie": 35,
#     "David": 40
# }
# res=koetrj(users)
# print(res)


import datetime
import calendar

# def week_day(day):
#     current_datetime = datetime.datetime.now()
#     day_of_week = current_datetime.weekday()
#     days_of_week_eng = list(calendar.day_name)
#     return days_of_week_eng[day_of_week]
#
#
# res=week_day(1)
# print(res)
