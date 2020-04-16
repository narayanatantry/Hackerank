p,d,m,s = list(map(int, input().split()))
c = p
count = 0
np = p

if p<=s:
    count =1
    while((c+np)<=s):
        if (np-d)>=m:
            np = np-d
        else:
            np =m
        count +=1
        c = c+np

print(count)
