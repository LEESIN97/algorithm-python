
def solution(clothes):
    answer = 0
    clothes_dict = {}
    for item_name, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = [item_name]
        else:
            clothes_dict[category].append(item_name)

    answer = 1
    for category in clothes_dict:

        answer *= (len(clothes_dict[category]) + 1)


    return answer - 1
