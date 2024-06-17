# states_of_america=['Delaware','Penssylvania']
# import random
# name_string=input()
# names=name_string.split(",")
# print(names)
# len_name=len(names)
#
# random_integer=random.randint(0, len_name - 1)
# print(random_integer)
#
# random_name = names[random_integer]
#
# print(f"{random_name} is going to buy the meal today!")



# Define the map
line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]

# Mapping for columns
column_labels = {'A': 0, 'B': 1, 'C': 2}

# Prompt user for the position
print("Hiding your treasure! X marks the spot.")
position = input("Enter the position (e.g., A1, B2): ")

# Convert position to indices and mark the spot with "X"
row = int(position[1]) - 1
column = column_labels[position[0].upper()]
map[row][column] = 'X'

# Print the map
for line in map:
    print("".join(line))

