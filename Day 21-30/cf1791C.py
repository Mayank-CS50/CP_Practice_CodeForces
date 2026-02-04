#1791C

for _ in range(int(input())):
    n=int(input())
    s=input()
    front=0
    back=n-1
    siz=0
    while front<=back:
        if s[front]==s[back]:
            siz=back-front+1
            break
        front+=1
        back-=1
    print(siz)
    
