a = int(input("Введите первое число: \n"))
b = int(input("Введите второе число: \n"))

if a > b:
    print("Победили хозяева счёт " + str(a) + ":" + str(b))

if a == b:
    print("Ничья, счёт " + str(a) + ":" + str(b))

if a < b:
    print("Победили гости счёт " + str(a) + ":" + str(b))