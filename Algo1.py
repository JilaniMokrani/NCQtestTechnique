def Solution (N,A):
    
    if 1 <= N <= 100000:
        print("N must be between 1 and 100 000.")
        return 0
    elif 1 <= A.length <= 100000:
        print("A has too many elements must not exced 100 000 elements.")
        return 0

    result = [0] * N

    for i in A:
        if 1 <= i <= N:
            result[ i-1 ] += 1
        elif i == N + 1:
            result = [ max(result) ] * N
        else:
            print("Operation number " + str(i+1) + "is wrong. \nIt must be between 1 and N+1.")
            return 0
    
    print(result)
    return result