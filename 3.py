def S(dlina, radius, visota):
    print(str(int(dlina) ** 2) + " - Площадь квадрата.")
    print(str(int(dlina) * int(visota) // 2) + " - Площадь треугольника.")
    print(str(int(radius) ** 2 * 3.14) + " - Площадь круга.")

S(dlina = input("Введите длинну: \n"), radius = input("Введите радиус: \n"), visota = input("Введите высоту: \n"))
