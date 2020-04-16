n = list(map(int,input().split()))
d = list(map(int,input().split()))
s,l = 0,[]
for i in range(len(d)):
    for j in range(i,len(d)):
        s = d[i]+d[j]
        l.append(s)
print(l)
