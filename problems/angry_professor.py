n = int(input())
def fun(d):
    t = 0
    for i in range(len(s)):
        if s[i]<=0:
            t = t+1
        if t>=d:
            return(print("YES"))
        else:
            return(print("NO"))



for i in range(n):
    l = list(map(int,input().split()))
    s = list(map(int,input().split()))
    z = l[1]
    fun(z)
