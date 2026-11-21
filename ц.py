age_groups = {
    "Олег": "дорослий",
    "Іра": "підліток",
    "Максим": "дитина",
    "Марія": "літня людина",
}

name = input("Введіть ім'я: ")

try:
    print(f"Вікова група: {age_groups[name]}")
except KeyError:
    print(f"Користувача {name} не знайдено")