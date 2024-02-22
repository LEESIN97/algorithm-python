s = list(input())
number_s = [0] * len(s)
for i in range(len(s)):
  number_s[i] = int(ord(s[i]) - ord('0'))

ans = number_s[0]

for data in number_s[1:]:
  if ans == 0:
    ans += data
    continue

  if data == 0:
    ans += data
  else:
    ans *= data



print(ans)
