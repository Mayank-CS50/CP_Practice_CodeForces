for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    diff=d-b
    if diff<=0:
        if a==c:
            print(0)
        elif a>c:
            print(a-c)
        else:
            print(-1)
    else:
        if a<c-diff:
            print(-1)
        else:
            val1=a-(c-diff)
            print(val1+diff)