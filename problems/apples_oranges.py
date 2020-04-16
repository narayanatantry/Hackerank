l= list(map(int,input().split()))
d = list(map(int,input().split()))
noao = list(map(int,input().split()))
m = list(map(int,input().split()))
n= list(map(int,input().split()))
print(m,n)
S1 =0
S2 =0
sum1 = 0
sum2 = 0
for i in range(len(m)):
    S1 = int(d[0] + m[i])
    if n[0]<S1<n[1]:
        sum1 = sum1 + 1

for j in range(len(n)):
    S2 = int(d[1] + n[j])
    if  n[0]<S2<n[1]:
        sum2 = sum2 + 1

print(sum1)
print(sum2)
