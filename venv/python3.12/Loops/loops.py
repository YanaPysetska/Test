# fruirs=['Apple', 'Peach', 'Pear']
# for i in fruirs:
#     print(i)
#     print(i + " Pie")
# import math
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# total_height=0
# for i in student_heights:
#     total_height+=i
# print(f'total_height={total_height}')
#
# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
# print(f"number of students = {number_of_students}")
#
#
# print(f'number_of_students={number_of_students}')
# average_height=total_height/number_of_students
# print(f'average_height={round(average_height)}')


student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

student_scores_max=student_scores[0]
for i in student_scores[1:]:
    if i>student_scores_max:
        student_scores_max=i
print(student_scores_max)

