for _ in range(int(input())):
    n,k=map(int,input().split())
    A=input()
    counter=0
    sleep=0
    while counter<n:
        # print(counter,sleep)
        if A[counter]=='1':
            if counter+k<n:
                if '1' in A[counter:counter+k]:
                    counter=A[counter:counter+k].index('1')+1
                else:
                    counter+=k            

        else:
            sleep+=1
        counter+=1
    print(sleep)