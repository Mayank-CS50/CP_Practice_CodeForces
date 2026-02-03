for _ in range(int(input())):
    n=int(input())
    count=0
    # for i in range(1,n+1):
    #     req=str(i)
    #     siz=len(list(req))  
    #     if req.count('0')==siz-1:
    #         count+=1
    # print(count)      
    req=0
    chala=1
    add=1
    while req<n:
        if chala>9:
            chala=1
            add*=10
        
        # print(req,add,chala,count)
        req+=add
        chala+=1
        count+=1

    print(count)