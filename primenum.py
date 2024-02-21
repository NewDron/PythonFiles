from math import *
def is_prime(num:int)->bool:
    """
    """
    p=True
    if num>=0 and num<1001:
        for i in range(2,num):
            if num%i==0:
                p=False
    return p
