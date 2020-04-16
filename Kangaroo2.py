main = list(map(int, input().split()))
x1,v1,x2,v2 = main[0],main[1],main[2],main[3]
s1 = x1 + v1
s2 = x2 + v2 
n1,n2 = 1,1
def rec(s1,s2):
    if n1 ==n2:
        print("YES")
        exit()
    else if n1 >100 and n2>100:
        print("NO")
    else :
        n1 = n1+1
        n2 = n2+1
        rec(s1+v1,s2+v2)
