n = int(input())
num = []
for i in range(n):
    x = int(input())
    num.append(x)
arr_pos = 0
arr_neg = 0
arr_zero = 0

for i in range(len(num)):
	if int(num[i])>0:
		arr_pos = arr_pos + int(num[i])
	elif int(num[i])<0:
		arr_neg = arr_neg + int(num[i])
	else:
		arr_zero = arr_zero + 1


arr_pos = float(arr_pos)
arr_neg = float(arr_neg)
arr_zero = float(arr_zero)

arr_zero = arr_zero/6
arr_neg = arr_neg/6
arr_pos = arr_pos/6

print(arr_pos)
print(abs(arr_neg))
print(arr_zero)
