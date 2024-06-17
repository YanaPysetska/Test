# Дан словарь с именем, фамилией
# и возрастом пяти пользователей.
# Выведите все элементы словаря в
# виде кортежа ключ-значение.

users_dict = {
    "user1": {"first_name": "Иван", "last_name": "Иванов", "age": 25},
    "user2": {"first_name": "Петр", "last_name": "Петров", "age": 30},
    "user3": {"first_name": "Мария", "last_name": "Сидорова", "age": 35},
    "user4": {"first_name": "Анна", "last_name": "Кузнецова", "age": 40},
    "user5": {"first_name": "Алексей", "last_name": "Смирнов", "age": 45}
}
for key, value in users_dict.items():
    print(f"Key: {key}, Value: {value}")
