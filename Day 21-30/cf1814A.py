for _ in range(int(input())):
    n,k=map(int,input().split())
    if k==1:
        print('YES')
    else:
        if n%2==0:
            print('YES')
        else:
            print('NO')