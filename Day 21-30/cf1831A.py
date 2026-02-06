for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    for i in A:
        print(n+1-i, end =' ')
    print() 