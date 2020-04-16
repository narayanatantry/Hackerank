l = int(input())
s,d = [],[]
for i in range(len(l)):
    n=0
    x = list(map(int, input().split())
    #d = list(map(float,x))
    for i in range(len(x)):
        d = sqrt(x[i])
        if (d-math.floor(x[i])==0 || d-math.floor(x[i])==0):
            n=n+1
    s.append(n)

for i in s:
    print(s[i])
