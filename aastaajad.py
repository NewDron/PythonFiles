from math import *
def season(number:int)->str:
    """

    """
    if number>0 and number<13:
        if number in [1,2,12]:
            s="Talv"
        elif number in [3,4,5]:
            s="Kevad"
        elif number in [6,7,8]:
            s="Suvi"
        else:
            s="Sügis"
    else:
        s="Vale number"
    return s

