
def birthday(ar,n):
	count = 1
	max = ar[0]
	for i in range(1,n):
		if ar[i]>max:
			max = ar[i]
			count = 1
		elif ar[i] ==max:
			count = count + 1
	return count

n = int(input())
a = list(map(int,input().rstrip().split()))
t = birthday(a,n)
print(t)



