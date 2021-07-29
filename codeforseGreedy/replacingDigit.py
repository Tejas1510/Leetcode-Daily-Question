s=input()
b=list(s)
t=input()
a=list(t)
a=sorted(a,reverse=True)
j=0
i=0
while(i<len(b) and j<len(a)):
    if(b[i]<a[j]):
        b[i]=a[j]
        j=j+1
        i=i+1
    else:
        i=i+1
        pass
print("".join(b))