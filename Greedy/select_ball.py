from itertools import combinations

n, m = map(int, input().split())
weight = list(map(int, input().split()))

result = list(combinations(weight, 2))
ans = 0
for data in result:
  if data[0] == data[1]:
    continue
  else:
    ans += 1

print(ans)
