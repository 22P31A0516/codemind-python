n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in a:
    if i==k+1:
        break
    else:
        s=s+i
print(s)