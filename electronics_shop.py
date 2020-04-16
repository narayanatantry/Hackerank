#problem link = https://www.hackerrank.com/challenges/electronics-shop/problem


def getmoneyspent(b,k,u):
    s,d,m = [],0,0
    for i in range(len(k)):
        for j in range(len(u)):
            if k[i]+u[j]<b:
                d = k[i]+u[j]
                if d>maxn:
                    maxn = d
            else:
                maxn = 0
    return(maxn)

bud = list(map(int, input().split()))
key = list(map(int, input().split()))
u   = list(map(int, input().split()))

ans = getmoneyspent(bud[0],key,u)
print(ans)
