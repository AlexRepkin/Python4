if __name__ == '__main__':
    print("Добрый день, пользователь! Здесь выполнено усложнённое задание:\nПолучить цифры числа, равного сумме "
          "заданных чисел.")
    a1 = int(input("Введите единицы первого числа - "))
    a2 = int(input("Введите десятки первого числа - "))
    a3 = int(input("Введите сотни первого числа - "))
    b1 = int(input("Введите единицы второго числа - "))
    b2 = int(input("Введите десятки второго числа - "))
    print("Ответ:\n ", a3 + ((a2+b2 + (a1+b1)//10)//10),
          ((a2+b2 + (a1+b1)//10) % 10), (a1+b1) % 10)
