s1=input().upper()
s2=input().upper()
n=len(s1)

f=0
for i in range(n):
    if s1[i]<s2[i]:
        f=-1
        break
    elif s1[i]>s2[i]:
        f=1
        break

print(f)