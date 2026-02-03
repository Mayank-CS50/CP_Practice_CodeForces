for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    found=False
    for i in range(n-1):
        if sum(A[:i])==A[i]:
            found=True
            break
    if found:
        print('NO')
    else:
        print('YES')