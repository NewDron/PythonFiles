#4

from random import *
L=int(input("Pikkus: "))
H=int(input("Laius: "))
for j in range(H):
    for x in range(L):
        print(randint(-10,100),end=" ")
    print()




#1

from random import *
n=randint(1,10)
x = [
    "/ \   ",
    "| |   ",
    "__    "
]

for i in x:
    print(i * n)


#2

Summa = []
while len(Summa) < 5:
    Kulu = float(input("Введите сумму трат за месяц: "))
    Summa.append(Kulu)
Keskmine = sum(Summa) / 12
print("Средняя сумма трат за год:", round(Keskmine, 2))



#5

from random import *

töötajad = int(input("Kogu töötajate arv: "))
A =1000

for i in range(töötajad):
    palk = randint(400,2000)
    print ("Palk: ",palk)
    if palk <= A:
        print("Töötaja on pensionär")
    else:
        print("Töötaja ei ole pensionär")


#3

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








