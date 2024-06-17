# lst = [
# 	[1, 2, 3],
# 	[4, 5, 6],
# 	[7, 8, 9],
# ]
# print(lst[0][1])
# print(lst[1][0])
# print(lst[2][1])

# lst = [
# 	['a', 'b'],
# 	{'c': 1, 'd': 2},
# 	{'e': 3, 'f': 4}
# ]
# print(lst[1]['c'])
# print(lst[2]['e'])


# lst = [
# 	[
# 		['a', 'b'],
# 		['c', 'd'],
# 	],
# 	[
# 		['e', 'f'],
# 		['g', 'h'],
# 	]
# ]
# print(lst[0][0][0]+lst[0][1][0]+
#       lst[1][0][1]+lst[1][1][0])



# lst = [
# 	[
# 		[1, 2],
# 		[3, 4],
# 	],
# 	[
# 		[5, 6],
# 		[7, 8],
# 	],
# ]
# print(lst[0][0][0]+lst[0][0][1]+
#       lst[0][1][0]+lst[0][1][1] +
#       lst[1][0][0]+lst[1][0][1]+
#       lst[1][1][0]+lst[1][1][1])


# lst = [
# 	[1, 2, 3],
# 	[4, 5, 6],
# 	[7, 8, 9]
# ]
#
# for i in lst:
#     for j in i:
#         print(j)


# lst = [
# 	[2, 4, 6],
# 	[3, 5, 7],
# 	[9, 12, 15]
# ]
# res=0
# for i in lst:
#     for j in i:
#         res+=j
# print(res)



# lst = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f'],
# 	['g', 'h', 'i']
# ]
# lst_one=[]
# for i in lst:
#     for j in i:
#         lst_one.append(j)
# # print(lst_one)
# my_string = ''.join(lst_one)
# print(my_string)

# lst = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i']
# ]
#
# result = ''
# for inner_list in lst:
#     for item in inner_list:
#         result += item
#
# print(result)


# lst = [
# 	[
# 		['q', 'w', 'e'],
# 		['r', 't', 'y'],
# 		['u', 'i', 'o'],
# 	],
# 	[
# 		['p', 'a', 's'],
# 		['d', 'f', 'g'],
# 		['h', 'j', 'k'],
# 	],
# 	[
# 		['l', 'z', 'x'],
# 		['c', 'v', 'b'],
# 		['n', 'm', 'q'],
# 	],
# ]
#
# for i in lst:
# 	for j in i:
# 		for el in j:
# 			print(el)



# lst = [
# 	[
# 		[1, 3],
# 		[5, 7],
# 	],
# 	[
# 		[2, 4],
# 		[6, 8],
# 	],
# ]
# res=0
# for i in lst:
# 	for j in i:
# 		for el in j:res+=el
# print(res)


# lst = [
# 	{
# 		'a': 1,
# 		'b': 2,
# 		'c': 3
# 	},
# 	{
# 		'a': 4,
# 		'b': 5,
# 		'c': 6
# 	},
# 	{
# 		'a': 7,
# 		'b': 8,
# 		'c': 9,
# 	},
# ]
# result=0
# for i in lst:
#     for key, value in i.items():
#         result+=value
# print(result)


# for i in lst:
#     for key, value in i.items():
#         print(key, value)


# lst=[]
#
# for i in range(0,3):
#     sub_lst=[]
#     for j in range(1,4):
#         sub_lst.append(j)
#     lst.append(sub_lst)
# print(lst)


# lst1 = []
# lst2 = ['a', 'b', 'c']
#
# for _ in range(2):
#     lst1.append(lst2.copy())
# print(lst1)

