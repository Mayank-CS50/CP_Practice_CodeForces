pos,neg=0,0
for _ in range(int(input())):
    a,b,c=map(str,input())
    if b=='+':
        pos+=1
    else:
        neg+=1
if pos>neg:
    print(pos-neg)
else:
    print(-(neg-pos))