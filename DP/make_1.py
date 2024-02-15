x = int(input())
d = [0] * (x + 1)

def top_down(x):
  if x == 2 or x == 3 or x == 5:
    return 1
  if d[x] != 0:
    return d[x]
  else:
    if x % 2 == 0:
      d[x] = 1 + min(top_down(x//2), top_down(x-1))
    elif x % 3 == 0:
      d[x] = 1 + min(top_down(x//3), top_down(x-1))
    elif x % 5 == 0:
      d[x] = 1 + min(top_down(x//5), top_down(x-1))
    else:
      d[x] = 1 + top_down(x-1)
  return d[x]

print(top_down(x))


