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
