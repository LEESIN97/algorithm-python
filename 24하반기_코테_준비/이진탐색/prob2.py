from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

lst = list(map(int, input().split()))

left_index = bisect_left(lst, x)
right_index = bisect_right(lst, x)
print(right_index - left_index)
