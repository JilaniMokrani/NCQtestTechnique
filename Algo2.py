def CountNumberOfWays(nbRungs, Modulo):

    print(nbRungs)

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
            result.append(CountNumberOfWays(A[i],B[i]))
        else:
            result.append(0)
            print("B[" + str(i) + "] = 0")

    print(result)
    return result

print(CountNumberOfWays(40,10000000))