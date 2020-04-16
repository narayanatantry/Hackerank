m = list(map(int , input().split()))
b = list(map(int , input().split()))
bt= int(input())
bc = 0
print(m,b,bt)
for i in range(len(b)):
    bc = bc + int(b[i])
k = int(m[1])
bc = bc - int(b[k])
bc = int(bc/2)

if bc==bt:
    print("Bon Appetit")
else :
    print(bc)
