while True:
    number = int(input("Введите число от 1 до 10:"))
    if  number >0 and number < 10 :
        print(number*2)
        break
    else:
        print("Число вне диапазона. Введите число от 1 до 10")