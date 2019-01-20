Mesich = int(input("Введите номер месяца: \n"))

if Mesich <= 0:
    print("Это число меньше 1!")

if Mesich >= 13:
    print("Это число больше 12!")

if Mesich >= 1:
    if Mesich <= 2:
        print("Зима.")

if Mesich >= 3:
    if Mesich <= 5:
        print("Весна.")

if Mesich >= 6:
    if Mesich <= 8:
        print("Лето.")

if Mesich >= 9:
    if Mesich <= 11:
        print("Осень.")

if Mesich >= 12:
    if Mesich <= 12:
        print("Зима.")
