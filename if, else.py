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
if a<0 or a>100:
    print("Viga tulemusega")
elif a>=0 and a<60:
    print("Hinne 2")
elif a >=60 and a<76:
    print("Hinne 3")
elif a >=76 and a<91:
    print("Hinne 4")
else:
    print("Hinne 5")
