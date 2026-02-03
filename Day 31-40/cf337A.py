n,m=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
start=0
back=n-1
chota=float('inf')
while back<m:
    temp=A[back]-A[start]
    if temp<chota:
        chota=temp
    start+=1
    back+=1

print(chota)