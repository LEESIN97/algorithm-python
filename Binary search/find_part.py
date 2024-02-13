def binary_search(target, array, start, end):
  mid = (start + end) // 2
  if start > end:
    return 'no'

  if array[mid] == target:
    return 'yes'
  elif array[mid] > target:
    return binary_search(target, array, start, mid - 1)
  elif array[mid] < target:
    return binary_search(target, array, mid + 1, end)


n = int(input())
product = list(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

product.sort()

start_index = 0
end_index = n - 1

for target_element in target:
  print(binary_search(target_element, product, start_index, end_index),
        end=' ')
