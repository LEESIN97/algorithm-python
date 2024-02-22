def solution(nums):
    answer = 0
    type_poketmon = set(nums)
    max = len(type_poketmon)
    if len(nums) // 2 > max:
        answer = max
    else:
        answer = len(nums) // 2

    return answer
