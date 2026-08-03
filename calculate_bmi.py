# Запрашиваем вес, повторяем запрос если введено не число
def get_weight():
        while True:
            try:
                weight = float(input("Введите свой вес: "))
                return weight
            except ValueError:
                print("Ошибка,введите число")
# Запрашиваем рост
def get_height():
        while True:
            try:
                height = float(input("Введите свой рост (метры и см через точку): "))
                return height
            except ValueError:
                print("Ошибка,введите число")
# Запрашиваем % жира
def get_bodyfat():
        while True:
            try:
                bodyfat = int(input("Введите свой % жира: "))
                return bodyfat
            except ValueError:
                print("Ошибка,введите число")
# Запрашиваем пол
def get_gender():
    while True:
        gender = input("Введите свой пол: ").lower().strip()
        if gender == "женщина" or gender == "woman":
            return "женщина"  # Приводим к одному виду
        elif gender == "мужчина" or gender == "man":
            return "мужчина"  # Приводим к одному виду
        else:
            print("Ошибка, введите пол (женщина/мужчина или woman/man)")
# Определяем категорию жира исходя из пола и % жира
def norm_bodyfat(gender, bodyfat):
    if gender == "woman" or gender == "женщина":
        bodyfat_dict = {
        "низкий % жира": (14, 20),
        "норма(жир)": (21, 31),
        "предожирение(жир)": (32, 35),
        "1 степень ожирения(жир)": (36, 40),
        "2 степень ожирения(жир)": (41, 50),
        "3 степень ожирения(жир)": (51, 100)
        }
    elif gender == "man" or gender == "мужчина":
        bodyfat_dict = {
        "низки % жира": (6, 13),
        "норма(жир)": (14, 24),
        "предожирение(жир)": (25, 25),
        "1 степень ожирения(жир)": (26, 30),
        "2 степень ожирения(жир)": (31, 40),
        "3 степень ожирения(жир)": (41, 100)
        }
# В словаре ищем нужную категорию
    for category, (low, high) in bodyfat_dict.items():
        if low <= bodyfat <= high:
            return(category)
# Высчитываем имт
def calculate_bmi(weight, height):
        bmi = weight / height ** 2
        if bmi < 18.5:
            return("У вас недостаток веса")
        elif bmi <= 24.9:
            return("У вас норма веса")
        elif bmi <= 29.9:
            return("У вас предожирение(вес)")
        elif bmi <= 34.9:
            return("У вас 1 степень ожирения(вес)")
        elif bmi <= 39.9:
            return("У вас 2 степень ожирения(вес)")
        else:
            return("У вас 3 степень ожирения(вес)")
# Выводим весь результат
def main():
    weight = get_weight()
    height = get_height()
    bodyfat = get_bodyfat()
    gender = get_gender()
    print(norm_bodyfat(gender, bodyfat))
    print(calculate_bmi(weight, height))
main()
# Предлагаем повторить
while True:
    again = input("Хотите еще раз? (да/нет)")
    if again == "нет":
        print("Пока!")
        break
    elif again == "да":
        main()
    else:
        print("Введите 'да' или 'нет'")