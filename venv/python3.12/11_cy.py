# Из словаря в предыдущей задачи
# выведите в столбик все имена
# пользователей. При этом пусть они
# все будут написаны с большой буквы.
users_dict = {
    "user1": {"first_name": "иван", "last_name": "Иванов", "age": 25},
    "user2": {"first_name": "петр", "last_name": "Петров", "age": 30},
    "user3": {"first_name": "мария", "last_name": "Сидорова", "age": 35},
    "user4": {"first_name": "анна", "last_name": "Кузнецова", "age": 40},
    "user5": {"first_name": "алексей", "last_name": "Смирнов", "age": 45}
}
for i in users_dict.values():
    print(i['first_name'].capitalize())

