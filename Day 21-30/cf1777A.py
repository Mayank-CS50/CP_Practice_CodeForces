def parityChk(a,b):
    if a%2==0 and b%2==0:
        return True
    elif a%2!=0 and b%2!=0:
        return True
    else:
        return False

for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    poi=0
    counter=0
    a,b=A[0],A[1]

    while poi<n:
        print(a,b,parityChk(a,b),counter)
        if not parityChk(a,b):
            counter+=1

            poi+=1
            a,b=A[poi],A[poi+2]

        else:
            a=a*b
            b=A[poi+2]
            
        
    print(counter)