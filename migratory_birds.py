x = int(input())
ML = list(map(int,input().split()))
from collections import Counter
t = dict(Counter(ML))
l = dict(sorted(t.items(), key=lambda t: t[1], reverse=True))
print(next(iter(l)))
