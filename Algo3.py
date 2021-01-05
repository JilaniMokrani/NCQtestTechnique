def Val(A,S):
    result = 0
    for i in range(A.length):
        result += A[i]*S[i]
    return abs(result)

def Solution(A):
    listOfS = [[1],[-1]]
    a= 1

    while a <= A.length:
        listOfS1 = listOfS

        for S in listOfS:
            S += [1]
        for S in listOfS1:
            S += [-1]
        
        listOfS += listOfS1
        print(listOfS)
        a+=1
    
    min = -1

    for S in listOfS:
        r = Val(A,S)
        if r == 0:
            print(0)
            return 0
        elif r < min:
            min = r
    
    print(min)
    return min