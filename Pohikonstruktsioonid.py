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




#8

from datetime import *
from random import *
arve_nr=date.today()#datetime.now()
tsekk="Arve: "+str(arve_nr)+"\nToode hind kogus Summa\n"
summa=0

tooded=["Piim","Leib","Kommid"] #len(tooded)=3

for i in range(len(tooded)):
    toode=tooded[i]
    hind=randint(50,150)/100
    v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
    if v =="jah":
        mitu=int(input("Mitu?"))
        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
        summa+=mitu*hind

tsekk+="Kokku maksta: "+str(summa)
print(tsekk)







pikkus_kokku = int(input("Введите длину куска ткани в метрах: "))
kasutatud_pikkus = 0
while pikkus_kokku - kasutatud_pikkus > 0:
    järgmine_pikkus = int(input("Введите длину следующего куска ткани в метрах (или 0 для завершения): "))
    if järgmine_pikkus <= pikkus_kokku - kasutatud_pikkus:
        kasutatud_pikkus += järgmine_pikkus
        print(f"Использовано {kasutatud_pikkus} метров ткани из {pikkus_kokku} метров.")
    else:
        print("Материала недостаточно.")
        break
print("Использование ткани завершено.")





Summa = []
while len(Summa) < 5:
    Kulu = float(input("Введите сумму трат за месяц: "))
    Summa.append(Kulu)
Keskmine = sum(Summa) / 12
print("Средняя сумма трат за год:", round(Keskmine, 2))



#Напишите программу для расчета количества сотрудников компании, чья зарплата превышает А евро и которые являются пенсионерами. Запросите у пользователя общее количество сотрудников и сгенерируйте зарплату, используя случайный метод.












print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a = abs(int(input("Введите целое число => ")))
        break
    except ValueError:
        print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=a
    b=a
    paaris =0
    paaritu = 0
    while b > 0:
        if b % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        b = b // 10
    
    print("Чётных цифр:"+str(paaris))
    print(f"Нечётных цифр: {paaritu}")
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()
    if c % 2 == 0:
        print("с - чётное число. Делим на 2.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
        if c % 2 == 0:
            c == c / 2
        else:
            c == (3*c + 1) / 2
        print(c,"\t")
    print()
    print("Гипотеза верна")
