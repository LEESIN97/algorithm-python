n, m = map(int, input().split())

card_table = [list(map(int, input().split())) for _ in range(n)]

row_min = [min(card_table[i]) for i in range(n)]

print(max(row_min))
