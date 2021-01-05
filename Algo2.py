import math as m

def CountNumberOfWays(nbRungs, Modulo):

    if nbRungs == 2:
        return 2 % Modulo    #either 1,1 or 2
    elif nbRungs == 1:
        return 1
    elif nbRungs == 0:
        return 0
    else: 
        return (CountNumberOfWays(nbRungs - 1, Modulo) + CountNumberOfWays(nbRungs - 2, Modulo)) % Modulo

def Solution(A, B):
    
    L = A.length
    result = []

    for i in range(L):
        if not B[i] == 0:
            result.append(CountTris(A[i],B[i]))
        else:
            result.append(0)
            print("B[" + str(i) + "] = 0")

    return result

def CountBis(nbRungs, Modulo):
    
    result = 0
    n = nbRungs
    p = 0

    a = m.factorial(n)
    b = 1
    c = a

    while n >= p:

        result = (result + a//b//c) % Modulo

        a = a // n
        b = b * (p + 1)
        if not (n-p-1 == 0 or n-p == 0):
            c = c // (n-p) // (n-p-1)
        else:
            c = 1

        n-=1
        p+=1

    return result % Modulo

def CountTris(nbRungs, Modulo):
    
    result = 0
    n = nbRungs
    p = 0

    c = 1

    while n >= p:
        result = result + (c % Modulo)
        if n-p-1 > 1:
            c = c * (n-p) * (n-p-1) // n //(p+1)
        else:
            c = 1

        n = n -1
        p = p + 1

    return result % Modulo