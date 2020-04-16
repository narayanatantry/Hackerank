l = int(input())
v = input()
V = list(v[::1])
s = 0
val =0
for i in range(len(V)):
    if V[i]=='U':
        s = s+1
        if s ==-1:
            val = val+0.5
    else:
        s = s-1
        if s==1:
            val = val+0.5

print(s)
print(int(val))
