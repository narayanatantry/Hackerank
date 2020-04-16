import collections
n = int(input())
l= list(map(int ,input().split()))
d = list(map(int,collections.Counter(l).values() ))
sum1 = 0
for i in range(len(d)):
    sum1 = sum1 + d[i]//2
print(sum1)
