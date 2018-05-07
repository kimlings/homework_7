import numpy as np

def erfenfa(f,a,b,w):
    k=0
    if f(a)*f(b)>0:
        return ("方程无解！")
    else:
            if f(a)*f(b)==0:
                if f(a)==0:
                    return (a,k)
                else:
                    return (b,k)
            else:
                while (True):
                     m = (a+b)/2
                     if abs(a-b)<=w:
                         return (m,k)
                         break
                     else:
                         if f(a)*f(m)>0:
                            a = m
                         else:
                             b = m
                     k = k+1
