for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%k!=0:
        print(1)
        print(n)
    else:
        for i in range(n,-1,-1):
            if i%k!=0:
                print(2)
                print(i,n-i)
                break