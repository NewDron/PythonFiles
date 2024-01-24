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
