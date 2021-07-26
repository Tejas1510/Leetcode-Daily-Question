n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(b[i]//a[i])
print(min(c))
