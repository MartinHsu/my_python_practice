from math import factorial
from decimal import Decimal, getcontext

getcontext().prec=10000

def calc_pi_bbp(n):
    #Calculate PI using BBP algroithm
    pi = Decimal(0)
    k = Decimal(0)
    for k in range(n):
        pi += 1/Decimal(16)**k\
            * ((Decimal(4)/(8*k+1))\
            - (Decimal(2)/(8*k+4))\
            - (Decimal(1)/(8*k+5))\
            - (Decimal(1)/(8*k+6)))
    return pi

def calc_to_file(n, file_name):
    pi = Decimal(0)
    pi = calc_pi_bbp(n)
    fout = open(file_name, 'wt')
    fout.write(str(pi))
    fout.close()