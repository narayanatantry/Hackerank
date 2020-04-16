n = list(map(int,input().split()))
d = list(map(int,input().split()))
s = 0
for i in range(len(d)):
    for j in range(i,len(d)):
        if (d[i]+d[j])%n[1]==0 and i<j:
            s = s+1

print(s)
