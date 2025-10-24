print("*** Arvude mang ***")
print()


while True:
    try:
        a = abs(int(input("Sisesta taisarv => ")))
        break
    except ValueError:
        print("See ei ole taisarv!")

if a == 0:
    print("Nulliga pole motet midagi teha")
else:
    print("Loendame, mitu on paaris ja mitu paaritu arvu")
    print()

    b = a
    paaris = 0
    paaritu = 0

  
    while b > 0:
        number = b % 10
        if number % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        b //= 10

    print("Paaris arvude kogus:", paaris)
    print("Paaritu on:", paaritu)
    print()


    print("*Umberpoorame* sisestatud arv:", a)
    b = 0
    originaal = a
    while a > 0:
        number = a % 10
        a //= 10
        b = b * 10 + number

    print()
    print("*Umberpooratatud* arv:", b)
    print()

    print("Toestame teoreem")
    print()

    c = b
    while c != 1:
        if c % 2 == 0:
            print(f"{int(c)} - Paaris arv. Jagame 2.")
            c = c / 2
        else:
            print(f"{int(c)} - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
            c = (3 * c + 1) / 2
    print("1 - Teoreem on toestatud")

