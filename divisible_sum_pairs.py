n = list(map(int,input().split()))
k = n[-1]
S = 0
O_P = 0
m = list(map(int,input().split()))
for i in range(len(m)):
    for j in range(i,len(m)):
        S = m[i]+m[j]
        print(S)
        if int(S)==:
            O_P = O_P +1

print(O_P)
