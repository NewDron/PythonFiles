#from random import *

#a=randint(-1,100)
#print("Juhuslik arv on", a)

#if a>0:
#    print(a,"suurem kui 0")
#else:
#    print(a,"väiksem kui 0 või võrdne 0-ga")

print("Kirjutage number 1-st kuni 100-ni:")
a = int(input())
    
#<0,>100 ei sobi, 0-59-"2",60-75-"3",76-90-"4",91-100-"5"
#if a<0 or a>100:
#    print("Viga tulemusega")
#elif a>=0 and a<60:
#    print("Hinne 2")
#elif a >=60 and a<76:
#    print("Hinne 3")
#elif a >=76 and a<91:
#    print("Hinne 4")
#else:
#    print("Hinne 5")

#5

temperatuur = float(input("Kirjutage toa temperatuur: "))

if  temperatuur > 18:
    print("Temperatuur on rohkem kui 18 kraadi.")
else:
    print("Temperatuur on alla 18 kraadi.")

#6

pikkus = float(input("Kirjutage oma pikkus: "))

if pikkus < 160:
    print("Sa oled luhike.")
elif pikkus >= 160 and pikkus <= 180:
    print("Sa oled keskmine.")
else:
    print("Sa oled pikk.")

#7

pikkus = float(input("Pikkus: "))
sugu = input("Sugu (M/F): ")

if sugu == "M":
    if pikkus < 160:
        print("Sa oled luhike.")
    elif pikkus >= 160 and pikkus <= 180:
        print("Sa oled keskmine.")
    else:
        print("Sa oled pikk.")
elif sugu == "F":
    if pikkus < 150:
        print("Sa oled luhike.")
    elif pikkus >= 150 and pikkus <= 170:
        print("Sa oled keskmine.")
    else:
        print("Sa oled pikk.")
else:
    print("Viga sugu valimisel.")

#8

piim_hind = 2.99
leib_hind = 1.99
munad_hind = 0.99

piim_qty = int(input("Palju pakke piima tahad osta? "))
leib_qty = int(input("Palju pakke leiba tahad osta? "))
munad_qty = int(input("Palju pakke mune tahad osta? "))

piim_cost = piim_hind * piim_qty
leib_cost = leib_hind * leib_qty
munad_cost = munad_hind * munad_qty

kokku = piim_cost + leib_cost + munad_cost

print("Summa kokku on", round(kokku, 2))

#9

side1 = float(input("Sisesta pikkus 1: "))
side2 = float(input("Sisesta pikkus 2: "))
side3 = float(input("Sisesta pikkus 3: "))
side4 = float(input("Sisesta pikkus 4: "))

if side1 == side2 == side3 == side4:
    print("See on ruut.")
else:
    print("See ei ole ruut.")

#10

num1 = float(input("Esimene number: "))
num2 = float(input("Teine number: "))

operation = input("Valige tehe (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Viga"

print("Tulemus on", result)

#11

birthday = int(input("Kirjuta oma sunnipaev: "))

if birthday % 10 == 0:
    print("See on juubel!")
else:
    print("See ei ole juubel!")

#12

price = float(input("Kirjuta toote hind €: "))

if price <= 10:  
    discount = price * 0.10
else:
    discount = price * 0.20

final_price = price - discount
print("Lopphind on", final_price, "€")

#13

sugu = input("Mis on kandidaadi sugu (mees/naine): ")

if sugu == "mees":
    age = int(input("Kui vana ta on: "))
    if age >= 16 and age <= 18:
        print("Ta sobib tiimi.")
    else:
        print("Ta ei sobi tiimi.")
elif sugu == "naine":
    print("Ta ei sobi tiimi.")
else:
    print("Viga!")

#14

num_people = int(input("Palju inimesi on: "))
bus_size = int(input("Palju mahub bussi: "))

num_buses = num_people // bus_size
remaining_people = num_people % bus_size

if remaining_people > 0:
    num_buses += 1

print("Vaja laheb busse:", num_buses)
print("Inimesi viimases bussis:", remaining_people)

