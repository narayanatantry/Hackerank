n = int(input())
bl = list(map(int,input().split()))
mn = list(map(int,input().split()))
m,n = mn[0],mn[1]
sum,t =0,0

for i in range(len(bl)):
    sum = bl[i]
    for j in bl[int(i):int(i+m+1)]:
        print(bl[j], bl[i])
        sum = sum + bl[j]
    if sum ==n:
        t = t+1

print(t)
