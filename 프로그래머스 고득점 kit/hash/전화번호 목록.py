def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        cnt = 0
        for j in range(len(phone_book[i])):
            if phone_book[i][j] == phone_book[i + 1][j]:
                cnt += 1
            else:
                break
        if cnt == len(phone_book[i]):
            answer = False


    return answer
