def fun(n, A):
    chota=float('inf')
    
    if 0 in A:
        return 0
    
    for i in range(n):
        if abs(A[i]) < abs(chota):
            chota=A[i]        
    return abs(chota)

n=int(input())
L=list(map(int,input().split()))
print(fun(n,L))