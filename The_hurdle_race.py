n = list(map(int , input().split()))
d = list(map(int , input().split()))
d.sort(reverse=True)
if d[0]>n[1]:
    s = d[0]-n[1]
    print(s)
else: print(0)
