s = int(input())
l = list(map(int,input().split()))
d,m = list(map(int,input().split()))
c = 0
if s = 1 and l==d:
    c = 1
else:
    for i in range(l):
        if l[i]+l[i+1]==d:
            c +=1
        else:
            continue

print(c)
