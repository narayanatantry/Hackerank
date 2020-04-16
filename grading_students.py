n = int(input())
t = []
m =[]
for i in range(n):
    l = input()
    m.append(l)

for i in range(len(m)):
    if int(m[i])<38:
        t.append(int(m[i]))
    else:
        mm =int(int(m[i])/5+1)
        if int(mm*5)-int(m[i])==int(3):
            t.append(int(m[i]))

        elif int(mm*5)-int(m[i])<int(3):
            m[i] = int(mm*5)
            t.append(int(m[i]))
        else:
            t.append(int(m[i]))


for i in range(len(t)):
    print(t[i])
