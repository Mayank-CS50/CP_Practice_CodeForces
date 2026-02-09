# for _ in range(int(input())):
#     a,b,c,d=map(int,input().split())
#     # diff=d-b
#     # if diff<=0:
#     #     if a==c:
#     #         print(0)
#     #     elif a>c:
#     #         print(a-c)
#     #     else:
#     #         print(-1)
#     # else:
#     #     if a<c-diff:
#     #         print(-1)
#     #     else:
#     #         val1=a-(c-diff)
#     #         print(val1+diff)
#     # v1=(c-a)
#     # v2=abs(d-b)
#     # print(a,b,c,d,v1,v2)
#     # if v1>v2:
#     #     print(-1)

#     # else:
#     #     if v1<0:
#     #         v1*=-2

#     #     print(2*v1-v2)
t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    k = d - b
    if k < 0:
        print(-1)
        continue
    
    if a + k < c:
        print(-1)
        continue
    
    print(k + (a + k - c))
