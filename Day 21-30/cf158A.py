n,m=map(int,input().split())
L=list(map(int,input().split()))
mid=L[m-1]
count=0
for i in L:
    if i >= mid and i!=0:
        count+=1
    # print(i,count)
print(count)