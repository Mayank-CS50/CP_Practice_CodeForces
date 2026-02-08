found=[0,0]
temp=False
for j in range(5):
    L=list(map(int,input().split()))   
    if not temp:
        for i in range(5):
            if L[i]==1:
                found=[j,i]
                if i>=2:
                    found[1]=i-2
                if j>=2:
                    found[0]=j-2
                temp=True
                break
    # print(L,found)
print(sum(found))
