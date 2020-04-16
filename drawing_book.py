gp = int(input())
ptf= int(input())
t =-1
if gp==ptf or gp==ptf+1:
    t = 0
elif ptf%2==0:
    while gp>ptf+1:
        t = t+1
        gp = gp-2
else:
    while gp>ptf:

        t = t+1
        gp = gp-2

print(t)
