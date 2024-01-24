#5


for i in range(1,11):
    for j in range(1,11):
        print(f"0",end="")
    print()


#4

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    



#3
from random import *
k=0
while True:
    k+=1
    print(f"{k}, ulesanne")
    a=randint(1,50)
    b=randint(1,50)
    p=5
    while True:
        v=int(input(f"{a}+{b}= "))
        p-=1
        if v==a+b:
            print("Oige vastus")
            break
        elif p == 0:
            print(f"{a}+{b}=(a+b)")
            break
        if k==3:  break



#ülesanne 2.2 sõne "q" lõpeb tsükkel
print("uus_programm")
sum_=0
i=0
while True:
    i+=1
    arv=input("Sisesta arv: ")
    if i>10: break
    try:
        arv=int(arv)
        sum_+=arv
    except:
        break
if sum_!=0:
    print(f"Summa= {sum_}")


#ülesanne 2.1 arv 777 lõpeb tsükkel
print("uus_programm")
sum_=0
i=0
while True:
    i+=1
    arv=int(input("Sisesta arv: "))
    if i>10: break
    if arv==777: break
    sum_+=arv
print(f"Summa= {sum_}")


#2

sum_ = 0
for i in range(10):
    arv=int(input("Sisesta arv: "))
    sum_ += arv
print(f"Summa= {sum_}")

#1

nimi=input("Palun sisesta oma nimi: ")
mitu=int(input("MIitu korda tervitada?" ))
for i in range(mitu):
    print(f"Ole tervitatud, {nimi}, {i+1} korda.")
