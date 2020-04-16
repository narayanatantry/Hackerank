t = int(input())
l = list(map(int,input().split()))
d = list(map(int,input().split()))
s,n,c,ll= d[0],d[1],0,0
for i


for i in range(len(l)-1):
    if l[i]+l[i+1] ==s or l[i]==s:
        c = c+1
        if n == c:
            break
print(c)


#put two loops
