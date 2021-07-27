t=int(input())
for i in range(t):
    parent=input()
    sub=input()
    c=0
    for i in range(len(parent)):
        if(parent.startswith(sub,i)):
            c=c+1
    print(c)
