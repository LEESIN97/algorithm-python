n = int(input())
score_list = []
for _ in range(n):
  name, score = input().split()
  score_list.append((name, int(score)))

score_list.sort(key=lambda x: x[1])

for i in range(n):
  print(score_list[i][0], end=' ')
