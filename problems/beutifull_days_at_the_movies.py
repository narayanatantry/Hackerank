n = list(map(int , input().split()))
def pal(y):
    rev =0
    while y>0:
        digit = y%10
        rev = rev*10+digit
        y = y//10
    return(rev)
d = []
for i in range(n[0],n[1]+1):
    d.append(int(i))
R=[]
S =0
T_s = 0
for i in range(len(d)):
    z = d[i]
    x = pal(z)
    R.append(x)
for i in range(len(d)):
    T_s = abs(d[i]-R[i])/n[2]
    if ((T_s).is_integer())==True:
        S = S+1
print(S)
