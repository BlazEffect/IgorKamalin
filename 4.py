def number():
    if Phone_number[0:4] == "+7928":
        print("Оператор телефона " + Phone_number + " - Мегафон")
    if Phone_number[0:4] == "+7951":
        print("Оператор телефона " + Phone_number + " - Tele2")
    if Phone_number[0:4] == "+7918":
        print("Оператор телефона " + Phone_number + " - МТС")
    if Phone_number[0:4] == "+7900":
        print("Оператор телефона " + Phone_number + " - Белайн")
    else:
        print("Я не знаю какой у тебя оператор")

Phone_number = input("Введите свой номер телефона:")
Phone_number = number()
