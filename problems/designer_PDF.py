n = list(map(int,input().split()))
a=[]
a = input().rstrip().split()
alphabet_map = {}
for i in range(len(n)):
    alphabet_map[chr(97+i)] = n[i]
d =[]
for i in a:
    d.extend(i.split())
print(d)
