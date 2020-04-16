n = int(input())
num = []
tot=0
num = input().split()
num.sort(reverse=True)
for i in range(n):
	if num[0]==num[i]:
		tot = tot +1
print(tot)

