from math import *
from datetime import *
def date_(päev:int,kuu:int,aasta:int)->bool:
    """
    """
    try:
        d=datetime.date(aasta,kuu,päev)
        print(d)
        tulemus=True
    except:
        tulemus=False
    return tulemus
