import random
import string

# 1. Создаем случайное количество словарей (от 2 до 10)
num_dicts = random.randint(2, 10)

# 2. Пустой список для хранения словарей
list_of_dicts = []

# 3. Генерируем каждый словарь
for i in range(num_dicts):
    # случайное количество ключей в словаре (от 2 до 5)
    num_keys = random.randint(2, 5)

    # выбираем случайные буквы из алфавита
    keys = random.sample(string.ascii_lowercase, num_keys)

    # создаем словарь с ключами и случайными значениями
    d = {k: random.randint(0, 100) for k in keys}

    # добавляем словарь в список
    list_of_dicts.append(d)

# 4. Печатаем, что получилось
print("Generated list of dicts:")
print(list_of_dicts)

# 5. Создаем пустой общий словарь
final_dict = {}

# 6. Проходим по каждому словарю в списке
for i, d in enumerate(list_of_dicts):
    for key, value in d.items():
        # если ключ еще не встречался — просто добавляем
        if key not in final_dict:
            final_dict[key] = (value, i + 1)
        else:
            # если ключ уже есть — проверяем, где значение больше
            if value > final_dict[key][0]:
                final_dict[key] = (value, i + 1)

# 7. Создаем финальный словарь с нужными именами ключей
result = {}
for key, (value, dict_num) in final_dict.items():
    # если ключ встречался в нескольких словарях — добавляем суффикс
    key_name = f"{key}_{dict_num}" if sum(key in d for d in list_of_dicts) > 1 else key
    result[key_name] = value

# 8. Печатаем финальный результат
print("\nFinal merged dict:")
print(result)

