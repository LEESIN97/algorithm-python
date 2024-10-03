n, k = map(int, input().split())
lsta = list(map(int, input().split()))
lstb = list(map(int, input().split()))

lsta.sort()
lstb.sort(reverse=True)

i = 0
while k != 0:
  if lstb[i] > lsta[i]:
    lsta[i], lstb[i] = lstb[i], lsta[i]
    k -= 1
    i += 1
  else:
    break

print(sum(lsta))
