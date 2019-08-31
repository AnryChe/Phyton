foo = int(input("Введите число от 1 до 10:"))
while foo <= 0 or foo >= 10:
    foo = int(input("Число вне диапазона. Введите число от 1 до 10:"))
else:
     print(foo**2)
