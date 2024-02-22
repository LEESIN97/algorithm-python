n = int(input())
warriors = list(map(int, input().split()))
warriors.sort(reverse=True)
number_of_group = 0

while warriors:
  warrior = warriors.pop()
  cnt = 1
  while warrior != cnt and warriors:

    warrior = warriors.pop()
    cnt += 1

  if warrior == cnt:
    number_of_group += 1

print(number_of_group)
