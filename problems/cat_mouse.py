x = int(input())
l=[]
for i in range(x):
    d = list(map(int,input().split()))
    x,y,z = d[0],d[1],d[2]
    if abs(d[0]-d[2])<abs(d[1]-d[2]):
        l.append("Cat a")
    elif abs(d[0]-d[2])>abs(d[1]-d[2]):
        l.append("Cat b")
    else:
        l.append("Mouse c")

for i in range(len(l)):
    print(l[i])
