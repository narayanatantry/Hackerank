n1 = 0
n2 = 0
l = list(map(int ,input().split()))
x1 = l[0]
v1 = l[1]
x2 = l[2]
v2 = l[3]
sum1 = x1
sum2 = x2
if  x2>x1 and v2>v1:
    print("NO")
    exit

while(sum1!=sum2):
    sum1 = sum1 + v1
    sum2 = sum2 + v2
    n1 = n1+1
    n2 = n2+1
    if sum1>100000 and sum2>100000:
        break
        


if n1==n2:
    print("YES")
else :
    print("NO")
