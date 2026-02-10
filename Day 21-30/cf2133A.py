for _ in range(int(input())):
    n=int(input())
    L=list(map(int,input().split()))
    from collections import Counter
    dic=Counter(L)
    found=False
    for i in dic:
        if dic[i]>1:
            found=True
            print('YES')
            break
    if not found:
        print('NO')
    
    # if L[-1]==L[0]:
    #     print('YES')
    # else:
    #     print('NO')