def fun():
    n,a,b=map(int,input().split())
    if a==b:
        if n!=a and n!=b:
            if n-a-b>1:
                return ('Yes')
            else:
                return ('No')
        else:
             return ('Yes')
    else:
        if n-a-b>1:
            return ('Yes')
        else:
            return ('No')
        
for _ in range(int(input())):
    print(fun())