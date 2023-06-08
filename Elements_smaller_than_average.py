n=int(input())
c=0
a=list(map(int,input().split()))
avg=sum(a)//len(a)
for i in a:
    if avg>=i:
        c+=1
print(c)