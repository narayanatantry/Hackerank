n = list(map(int,input().split()))
k = n[-1]
S = 0
O_P = 0
j = 1
m = list(map(int,input().split()))
for i in range(len(m)):
    sum = n[i] + n[j]
    j = j+1



print(O_P)
