import random

punkte = 0
küsimusi = 10
print("Matemaatika test!")

tase = int(input("Valige tase (1, 2, 3): "))

for _ in range(küsimusi):
    if tase == 1:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif tase == 2:
        num1, num2 = random.randint(10, 100), random.randint(10, 100)
    elif tase == 3:
        num1, num2 = random.randint(100, 1000), random.randint(100, 1000)

    operaatorid = ['+', '-', '*', '/']
    operaator = operaatorid[random.randint(0, 3)]

    print(f"Mis on {num1} {operaator} {num2}?")

    if operaator == '+':
        õige_vastus = num1 + num2
    elif operaator == '-':
        õige_vastus = num1 - num2
    elif operaator == '*':
        õige_vastus = num1 * num2
    elif operaator == '/':
        if num2 != 0:
            õige_vastus = num1 / num2
        else:
            õige_vastus = None

    sisestatud_vastus = input("Kirjuta oma vastus: ")

    try:
        sisestatud_vastus = float(sisestatud_vastus)
        if sisestatud_vastus == õige_vastus:
            punkte += 1
            print("Õige vastus!")
        else:
            print("Vale vastus!")
    except ValueError:
        print("Palun kirjuta number.")

print(f"Õigeid vastuseid: {punkte}/{küsimusi}")

protsendid = (punkte / küsimusi) * 100
if protsendid < 60:
    print("Hinne: 2")
elif 60 <= protsendid < 75:
    print("Hinne: 3")
elif 75 <= protsendid < 90:
    print("Hinne: 4")
else:
    print("Hinne: 5")


