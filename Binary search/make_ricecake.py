def binary_search(target, array, start, end):
  result = 0
  while start <= end:
      mid = (start + end) // 2
      sum = 0
      for x in array:
          if x > mid:
              sum += x - mid
      if sum < target:
          end = mid - 1
      else:
          result = mid
          start = mid + 1
  return result

n, m = map(int, input().split())
rcake_array = list(map(int, input().split()))
rcake_array.sort()
print(binary_search(m, rcake_array, 0, rcake_array[n - 1]))

