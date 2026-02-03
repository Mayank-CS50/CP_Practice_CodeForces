for _ in range(int(input())):
    n=int(input())
    L=list(map(int,input().split()))
    found=True
    uniform=L[0]^L[1]
    
    for i in range(2,n):
        uniform^=L[i]
        if uniform==uniform^L[i]:
            found=False
            break
        else:
            uniform^=L[i]
    if not found:
        print()
    else:
        print()