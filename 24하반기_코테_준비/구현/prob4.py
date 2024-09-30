s = list(map(str, input()))

digit_lst = [chr for chr in s if chr.isdigit()]
char_lst = [chr for chr in s if chr.isalpha()]

char_lst.sort()
digit_lst.sort()

char_lst.extend(digit_lst)

print(''.join(char_lst))
