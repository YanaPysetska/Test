num = 1

# def func():
# 	print(num)
#
# func()

# основной учебник 2

# def func(*args):
# 	return tuple(args)
#
# res=(func('Yana','Boris', 'Aboba'))
# print(type(res))


# def func(**kvargs):
# 	print(kvargs)
#
# func(
#     day1='Monday',
#     day2='Tuesday',
#     day3='Wednesday',
#     day4='Thursday',
#     day5='Friday',
#     day6='Saturday',
#     day7='Sunday'
# )

#
# def func(**kvargs):
# 	print(kvargs)
#
# func(
#     yana=30,
#     boris=35,
#     aboba=26
# )


# def func(*, name='user1', age='18'):
# 	return 'Username is ' + name + ' age is ' + age
#
# print(func(name='john'))


# def month(*args):
# 	'принимать параметром список названий месяцев и выводить их с заглавной буквы'
# 	new_list=[]
# 	for i in args:
# 		new_list.append(i.title())
# 	return new_list
#
# months_ukr = [
#     "cічень",
#     "лютий",
#     "березень",
#     "Квітень",
#     "Травень",
#     "Червень",
#     "Липень",
#     "Серпень",
#     "Вересень",
#     "Жовтень",
#     "Листопад",
#     "Грудень"
# ]
# res=month(*months_ukr)
# print(res)
#
# help(month)

# help(sum)
# help(len)



# def func(num, clb):
# 	return clb(num)
# clb = lambda num: num+1
# print( func(2, clb) )

#
# def func(num, clb1, clb2):
# 	return (clb1(num), clb2(num))
# print( func(2, lambda num:num + 1, lambda num:num - 1) )


# def func(num1, num2, clb):
# 	res = clb(num1) + num2
# 	return res
# print(func(2, 6, lambda num:num ** 3 ))

# lst = [1, 2, 3, 4, 5]
# res = map(lambda num:num+1, lst)
# print(list(res))



# lst = ['123', '456', '789']
# res = map(lambda txt:txt[::-1], lst)
# print(list(res))

# lst = [1, 2, 3, 4, 5]
# res=filter(lambda num: num%2!=0, lst)
# print(list(res))

# lst = ['abcd', 'ab', 'c', 'de', 'bc']
# res=filter(lambda txt:len(txt)==2,lst)
# print(list(res))

# def func():
#     global num
#     num=4
#     num *= 2
#     return num
# print(func())


# num = 10
#
# def func():
#     global num
#     num -= 3
#     return num
#
# print(func())


# def outer(lst):
#     def inner(txt):
#         return txt.capitalize()
#     res = []
#     for i in lst:
#         res.append(inner(i))
#     return res
#
# print(outer(["hello", "world"]))

# def func2(iter):
#     def func1(num):
#         if num > 0:
#             num += 2
#         return num
#
#     res = []
#     for el in iter:
#         res.append(func1(el))
#     return res
# print(func2([1, -2, 3, 0, 5]))

# 20


# height = input()
# weight = input()
# bmi=int(weight)/float(height)**2
# print(int(bmi))

# num = 3
#
# def outer():
#     global num
#     num += 1
#     tst = num
#
#     def inner():
#         nonlocal tst
#         tst = tst ** 3
#
#     inner()
#     return tst
#
# print(outer())
#
# 22

# age = input()
# years=(90-int(age))
# x=years*52
# print(f"You have {x} weeks left.")


# bill=input('Welcome to the tip calculator!\nWhat was the total bill? $')
# percent=input('How much tip would you like to give? 10, 12, or 15? ')
# people=input("How many people to split the bill?")
# percent_result=(int(percent)/100)*int(bill)
# result=(int(bill)+int(percent_result))/int(people)
# print(f'Each person should pay: {result}')




# year=int(input())
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print('leap year')
#         else:
#             print('not leap year')
#     else:
#         print('leap year')
#
# else:
#     print('not leap year')
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L")
# add_pepperoni = input('Do you want pepperoni? Y or N')
# extra_cheese = input('Do you want extra cheese? Y or N')
# bill = 0
#
# if size == 'S':
#     bill = 15
# elif size == 'M':
#     bill = 20
# elif size == 'L':
#     bill = 25
#
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == 'Y':
#     bill += 1
#
# print(f'Your final bill is: ${bill}.')


# print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# lower_names=(name1+name2).lower()
# t=lower_names.count('t')
# r=lower_names.count('r')
# u=lower_names.count('u')
# e=lower_names.count('e')
# first=t+r+u+e
# l=lower_names.count('l')
# o=lower_names.count('o')
# v=lower_names.count('v')
# e=lower_names.count('e')
# second=l+o+v+e
# score = int(str(first) + str(second))
# if score < 10 and score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif 40 >= score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")



