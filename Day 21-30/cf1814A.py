for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%2==0 or (n-k)%2==0:
        print('YES')
    else:
        print('NO')
    # if k==1:
    #     print('YES')
    # else:        
    #     while n%k==0:
    #         n//=k

    #     print(n)
    #     # while n%2==0:
    #     #     n//=2
    #     # print(n)

    #     if n%2==0:
    #         print('YES')
    #     else:
    #         print('NO')