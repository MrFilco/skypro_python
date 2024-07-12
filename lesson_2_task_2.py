def is_year_leap(year):
    return year % 4 == 0

# Выбираем любой год для проверки
year_to_check = 2020

# Вызываем функцию и сохраняем результат в переменную
is_leap = is_year_leap(year_to_check)

# Выводим результат в консоль
print(f"Год {year_to_check}: {is_leap}")