for _ in range(int(input())):
    n=int(input())
    found=False
    while n%2==0:
        n//=2
    if n>1:
        print('YES')
    else:
        print('NO')
    # if n%2!=0:
    #     print('YES')
    # else:
    #     for i in range(3,int(math.sqrt(n)),2):
    #         if n%i==0:
    #             found=True
    #             break

    #     if found:
    #         print('YES')
    #     else:
    #         print('NO')