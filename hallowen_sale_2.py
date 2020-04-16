p,d,m,s = list(map(int,input().split()))
def Mist(p,d,m,s):
    count = 0
    while s>=m:
        if(p-d)>m:
            s= s-(p-d)
            count++
        else:
            d=m
            s = s=(p-d)
            count++
    return(count)
l = Mist(p,d,m,s)
print(l)
