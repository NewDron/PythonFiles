from random import *
from string import *

#11

tähestik = 'abcdefghijklmnopqrstuvwxyz'
n = 26
tähed = [tähestik[i] for i in range(n)]
print("Tähed:", tähed)
korduvad = []
for i in range(n):
    korduvad.append(tähestik[i] + tähestik[i] * i)
print("Korduvad tähed:", korduvad)

#12

import random
juhuslik_number = [random.randint(1, 100) for i in range(10)]
print("Juhuslikud numbrid:", juhuslik_number)
min_index = juhuslik_number.index(min(juhuslik_number))
max_index = juhuslik_number.index(max(juhuslik_number))
juhuslik_number[min_index], juhuslik_number[max_index] = juhuslik_number[max_index], juhuslik_number[min_index]
print("Loendi miinimaalse ja maksimaalse elemendi vahetus:", juhuslik_number)

#7

numbrid = [3, -5, 1, -8, 6, -2]

kahanev = []
while numbrid:
    max_num = numbrid[0]
    for num in numbrid:
        if abs(num) > abs(max_num):
            max_num = num
    kahanev.append(max_num)
    numbrid.remove(max_num)
print("Sorteeritud numbrite nimekiri kahaneva absoluutväärtuse järgi:", kahanev)

numbrid = [3, -5, 1, -8, 6, -2]

kasvav = []
while numbrid:
    min_num = numbrid[0]
    for num in numbrid:
        if abs(num) < abs(min_num):
            min_num = num
    kasvav.append(min_num)
    numbrid.remove(min_num)
print("Sorteeritud numbrite nimekiri kasvava absoluutväärtuse järgi:", kasvav)

#6

#arvud=[1,2,3,4,5,6,7,8,9,122,44,5]
#max_=max(arvud)
#indeks=arvud.index(max_)
#max_=int(max_/len(arvud))
#arvud[indeks]=max_
#print(arvud)

#5

#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#n=int(input("Mitu paari vahetada "))
#if len(rida)//2>=n:
#    for i in range(n):
#        abi=rida[i]
#        rida[i]=rida[len(rida)-1-i]
#        rida[len(rida)-1-i]=abi
#else:
#    print("Liiga vähe elemente")
#    print(rida)

#4

#Indeksid=["Tallinn", "Narva", "Tartu", "Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa", "Lääne-Virumaa", "Jõgevamaa", "Tartumaa", "Põlvamaa", "Võrumaa", "Valgamaa","Viljandimaa", "Järvamaa", "Harjumaa", "Raplamaa", "Pärnumaa", "Läänemaa", "Hiiumaa", "Saaremaa"]
#while True:
#    indeks=input("Indeks: ")
#    if len(indeks)==5 and indeks.isdigit() and indeks[0]!="0":
#        print("Sa elad piirkonnas ",Indeksid[int(indeks[0])-1])

#    else:
#        print:("Sisesta indeks uuesti: ")

#3
##while True:
##    try:
#        N=int(input("Mitu rida loome?" ))
#        break
#    except:
#        print("Vale tüüp")
#while true:
#    try:
#        S=input("Mis sümbol korrutame? ")
#        if S in punctuation:
#            break
#        else:
#            print("Vale sümbol")
#    except:
#        print("Vale sümbol")
#for i in range(N):
#    print(randint(1,25)*5)

#2
#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ")
#    nimed.append(nimi)

#print("Sisestatud: ",nimed)
#nimed.sort()
#print("Sorteeritud: ",nimed)
#print("Viimasena oli lisatud: ",nimi)
#nimi=input("Mis nimi on vaja asendada?")
#indeks=nimed.index(nimi)
#uus_nimi=input("Uus nimi: ")
##nimed[indeks]=uus_nimi
#nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
#nimed=set(nimed)
#print(nimed)
#vanused=[]
#for i in range(5):
#    v=input("Sisesta vanus: ")
#    vanused.append(v)
#sum_=sum(vanused)
#min_=min(vanused)
#max_=max(vanused)
#kesk=sum_/len(vanused)
#print("Keskmine on {kesk}, \nSuurim on {max_}, \nVäiksem on {min_}, \nSumma on {sum_}")

#1
#from string import punctuation
#vokaalid=["a","e","i","o","u","õ","ä","ö","ü"]
#konsonandid=["l", "m", "n", "r", "v", "j", "g", "b", "d", "k", "p", "t", "s", "h", "f", "š", "z", "ž"]
#märgid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta tekst: " ) #mama
#print(tekst)
#tekst_list=list(tekst) #["m","a","m","a"]
#print(tekst_list)
#for element in tekst_list:
#    if element.lower() in vokaalid:
#        v+=1
#    elif element.lower() in konsonandid:
#        k+=1
#    elif element in märgid:
#        m+=1
#    elif element==" ":
#        t+=1
#print("Vokaalid: ",v)
#print("Konsonandid: ",k)
#print("Märgid: ",m)
#print("Tühikud: ",t)
