#2
nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ")
    nimed.append(nimi)

print("Sisestatud: ",nimed)
nimed.sort()
print("Sorteeritud: ",nimed)
print("Viimasena oli lisatud: ",nimi)
nimi=input("Mis nimi on vaja asendada?")
indeks=nimed.index(nimi)
uus_nimi=input("Uus nimi: ")
#nimed[indeks]=uus_nimi
nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
nimed=set(nimed)
print(nimed)
vanused=[]
for i in range(5):
    v=input("Sisesta vanus: ")
    vanused.append(v)
sum_=sum(vanused)
min_=min(vanused)
max_=max(vanused)
kesk=sum_/len(vanused)
print("Keskmine on {kesk}, \nSuurim on {max_}, \nVäiksem on {min_}, \nSumma on {sum_}")



#1
from string import punctuation
vokaalid=["a","e","i","o","u","õ","ä","ö","ü"]
konsonandid=["l", "m", "n", "r", "v", "j", "g", "b", "d", "k", "p", "t", "s", "h", "f", "š", "z", "ž"]
märgid=punctuation
v=k=m=t=0
tekst=input("Sisesta tekst: " ) #mama
print(tekst)
tekst_list=list(tekst) #["m","a","m","a"]
print(tekst_list)
for element in tekst_list:
    if element.lower() in vokaalid:
        v+=1
    elif element.lower() in konsonandid:
        k+=1
    elif element in märgid:
        m+=1
    elif element==" ":
        t+=1
print("Vokaalid: ",v)
print("Konsonandid: ",k)
print("Märgid: ",m)
print("Tühikud: ",t)
