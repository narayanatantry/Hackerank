def getmoneyspent(b,k,u):
    s,d = [],0
    if max(k)+max(u)<b:
        return(max(k)+max(u))
    else :
        return(0)

bud = list(map(int, input().split()))
key = list(map(int, input().split()))
u   = list(map(int, input().split()))

ans = getmoneyspent(bud[0],key,u)
print(ans)
