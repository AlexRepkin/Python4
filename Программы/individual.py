if __name__ == '__main__':
    print("Добрый день, пользователь! Тут находятся мои индивидуальные задания.")
    print("Задание №1: Даны два числа. Найти среднее арифметическое и среднее геометрическое их модулей.")
    value1 = abs(int(input("Введите первое число - ")))
    value2 = abs(int(input("Введите второе число - ")))
    answer1 = (value1 + value2) / 2
    answer2 = pow((value1 * value2), 0.5)
    print("Ответ:\nАрифметическое значение - ", answer1, "\nГеометрическое значение - ", answer2, ".")
    print("Задание №2: Даны стороны прямоугольника. Найти его периметр и длину диагонали.")
    value1 = int(input("Первая сторона - "))
    value2 = int(input("Вторая сторона - "))
    answer1 = value1 * 2 + value2 * 2
    answer2 = pow((pow(value1, 2) + pow(value2, 2)), 0.5)
    print("Ответ:\nПериметр - ", answer1, "\nДиагональ - ", answer2, ".")
    print("Задание №3: Даны стороны треугольника , и найти площадь треугольника по формуле Герона")
    value1 = int(input("Первая сторона - "))
    value2 = int(input("Вторая сторона - "))
    value3 = int(input("Третья сторона - "))
    answer1 = (value1 + value2 + value3) / 2
    answer2 = pow((answer1 * (answer1 - value1) * (answer1 - value2) * (answer1 - value3)), 0.5)
    print("Ответ:\nПлощадь треугольника - ", answer2, ".")
    print("Задание №4: Даны два числа. Найти их сумму, разность, произведение, а также частное от деления первого "
          "числа на второе.")
    value1 = int(input("Первое число - "))
    value2 = int(input("Второе число - "))
    answer1 = value1 + value2
    answer2 = value1 - value2
    print("Ответ:\nSumm - ", answer1, "\nDifference - ", answer2, )
    answer1 = value1 * value2
    answer2 = value1 / value2
    print("Multiplication - ", answer1, "\nQuotient - ", answer2, )
