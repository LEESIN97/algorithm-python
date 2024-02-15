# n, m = map(int, input().split())
# money_type = []
# for _ in range(n):
#   money_type.append(int(input()))

# d = [0] * 10001
# for money in money_type:
#   d[money] = 1

# min_money = min(money_type)

# for i in range(min_money + 1, m + 1):
#   if i in money_type:
#     continue
#   min = 999999999
#   cnt = 0
#   for money in money_type:
#     if (i - money) % money == 0:
#       cnt += 1
#       if min > (d[i - money] + 1):
#         min = d[i - money] + 1
#     else:
#       continue
#   if cnt != 0:
#     d[i] = min
#   else:
#     d[i] = -1

# print(d[m])



n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [100001] * (m + 1)

d[0] = 1
for i in range(n):
	for j in range(array[i], m + 1):
		if d[j - array[i]] != 10001:
			d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
	print(-1)
else: print(d[m])


