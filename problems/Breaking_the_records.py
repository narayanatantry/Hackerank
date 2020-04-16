n = int(input())
x = list(map(int , input().split()))
high = x[0]
low = x[0]
H_T = 0
L_T = 0
for i in range(1,len(x)):
    if high<x[i]:
        high = x[i]
        H_T = H_T + 1
    elif low>x[i]:
        low = x[i]
        L_T = L_T + 1

print(H_T,L_T)
