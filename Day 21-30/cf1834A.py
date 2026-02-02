for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    pos=A.count(1)
    neg=A.count(-1)
    if pos>=neg:
        if neg%2==0:
            print(0)
        else:
            print(1)
    else:
        countt=0
        while True:
            pos+=1
            neg-=1
            countt+=1
            if pos>=neg:
                break

        if neg%2==0:
            print(countt)
        else:
            print(countt+1)
            
        # diff=neg-pos
        # if (neg-diff)%2==0:
        #     print(diff)
        # else:
        #     print(diff-1)