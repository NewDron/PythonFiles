#1 Juku laheb kinno

nimi = input("Mis on su nimi? ")
if nimi.upper()=="JUKU":
	print("Laheme kinno")
	vanus=int(input("Kui vana sa oled? "))
	if vanus<0 or vanus>120:
		vastus="viga vastusega"
	elif vanus<6:
		vastus="tasuta pilet"
	elif vanus<14:
		vastus="lastepilet"
	elif vanus<65:
		vastus="taispilet"
	elif vanus<120:
		vastus="sooduspilet"
	print("On vaja Jukule osta", vastus)
else:
	print("Joonistame")

#2

n1 = input("Esimene nimi: ")
n2 = input("Teine nimi: ")
if n1.upper()=="A" and n2.upper()=="B" or n1.upper()=="B" and n2.upper()=="A":
	print("Pinginaabrid")
else:
	print("Nad ei ole naabrid")
if n1.upper() in ["A","B"] and n2.upper() in ["A","B"]:
	print("Pinginaabrid")
else:
	print("Nad ei ole naabrid")

#3

sein1 = float(input("Esimese seina pikkus: "))
sein2 = float(input("Teise seina pikkus: "))
S = sein1 * sein2
print("Pindala ruutmeetrites on: ", S)
vastus = input("Soovite teha remonti? ")
if vastus.lower()=="jah":
	hind = float(input("Palju maksab ruutmeeter? "))
	summa = hind * S
	print("Ruutmeetri hind: ", summa)

#4

hind = float(input("Hind: "))
if hind>700:
	hind*=0.7
print("Uus hind: ", hind)

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

