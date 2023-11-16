if __name__ == '__main__':
    print("Good day, user! This time, we need you to enter some values for us. Let the experiment begin!")
    first = int(input("Your first number is - "))
    second = int(input("Your second number is - "))
    third = int(input("Your third number is - "))
    fourth = int(input("Your fourth number is - "))
    first_sum = first + second
    second_sum = third + fourth
    answer = first_sum / second_sum
    print("Interesting...\nSo, according to our calculations, the answer is - ", round(answer, 2), ".")
    input()
