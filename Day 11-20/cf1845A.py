for _ in range(int(input())):
    n,k,x=map(int,input().split())
    
    if k>1:
        if x!=1:
            print('YES')
            print(n)
            print(n*'1 ')
            
        elif x==1:
            if n%2==0:
                print('YES')
                print(n//2)
                print((n//2)*'2 ')
            else:
                if k>2:
                    print('YES')
                    print(n//2)
                    print(((n//2)-1)*'2 '+'3')
                
                else:
                    print('NO')
    else:
        if k==1:
            if x==1:
                print('NO')
            else:
                print('YES')
                print(n)
                print(n*'1 ')