n=int(input())
L=list(map(int,input().split()))

maxx=float('-inf')
front=0
back=1
count=0
while back<=n:
    if L[front]<=L[back]:
        count+=1
        back+=1
    else:
        count=0
        front=back-1
        back=front+1
    if count>maxx:
        maxx=count
print(maxx)
