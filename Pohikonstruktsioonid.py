#print("Tere maailm!")
#nimi = input("Mis on sinu nimi?")
#vanus = int(input("Kui vana sa oled?"))

#print("Tere "+nimi+"! Sa oled "+str(vanus)+" aastat vana!")
#print("Tere ",nimi,"! Sa oled ",vanus," aastat vana!")
#print("Tere {0}! Sa oled (1) aastat vana!".format(nimi,vanus))

#print(type(nimi))
#print(type(vanus))

#arv1=float(input("Arv 1:"))
#t=input("Tehe: ")
#arv2=float(input("Arv 2:"))
#vastus=eval(str(arv1)+t+str(arv2))
#print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))

#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True

#print(type(vanus))
#print(type(eesnimi))
#print(type(pikkus))
#print(type(kas_käib_koolis))

#from random import * #koik funktsioonid mis on moodulis
#kogus=randint(1,100)
#print("Kokku on",kogus,"kommid")
#mitu=int(input("Mitu kommi tahad?"))
#print(kogus-mitu, "Komme jaanud")

#from math import *
#l=float(input("Umbermoot:"))
#d=l/pi          #3.14...
#print("Labimoot= ", d)

#from random import *
#1 Juku laheb kinno
#nimi = input("Mis on su nimi? ")
#if nimi.upper()=="JUKU":
#	print("Laheme kinno")
#	vanus=int(input("Kui vana sa oled? "))
#	if vanus<0 or vanus>120:
#		vastus="viga vastusega"
#	elif vanus<6:
#		vastus="tasuta pilet"
#	elif vanus<14:
#		vastus="lastepilet"
#	elif vanus<65:
#		vastus="taispilet"
#	elif vanus<120:
#		vastus="sooduspilet"
#	print("On vaja Jukule osta", vastus)
#else:
#	print("Joonistame")

#2

#n1 = input("Esimene nimi: ")
#n2 = input("Teine nimi: ")
#if n1.upper()=="A" and n2.upper()=="B" or n1.upper()=="B" and n2.upper()=="A":
#	print("Pinginaabrid")
#else:
#	print("Nad ei ole naabrid")
#if n1.upper() in ["A","B"] and n2.upper() in ["A","B"]:
#	print("Pinginaabrid")
#else:
#	print("Nad ei ole naabrid")

#3

#sein1 = float(input("Esimese seina pikkus: "))
#sein2 = float(input("Teise seina pikkus: "))
#S = sein1 * sein2
#print("Pindala ruutmeetrites on: ", S)
#vastus = input("Soovite teha remonti? ")
#if vastus.lower()=="jah":
#	hind = float(input("Palju maksab ruutmeeter? "))
#	summa = hind * S
#	print("Ruutmeetri hind: ", summa)

#4

hind = float(input("Hind: "))
if hind>700:
	hind*=0.7
print("Uus hind: ", hind)
