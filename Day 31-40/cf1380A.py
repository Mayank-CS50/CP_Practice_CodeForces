#cf1380A Three Indices
import sys
input=sys.stdin.readline
t=int(input())

def fun(n,A):
    found=False

    i,j,k=0,1,2
    while k<n:
        if A[i]<A[j]>A[k]:
                    print('YES')
                    print(i+1,j+1,k+1)
                    found=True
                    break
        i+=1
        j+=1
        k+=1
    if not found:
          print('NO')
    # for i in range(n-2):
    #     for j in range(i+1,n-1):
    #         for k in range(j+1,n):
    #             if A[i]<A[j]>A[k]:
    #                 print('YES')
    #                 print(i,j,k)
    #                 found=True
    #                 break
    #         if found:
    #             break
    #     if found:
    #         break
    # if not found:
    #     print('NO')
                    


for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    fun(n,A)