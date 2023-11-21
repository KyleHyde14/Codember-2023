import re

with open('encrypt.txt', 'r') as file:
    key_list = []

    for line in file:
        key_list.append(line[:-1])



def checkPass(key_list):
    invalids = []
    range_regex = r'^[0-9]+-[0-9]+ '
    letter_regex = r' [a-z]'
    pass_regex = r': [a-z]+'

    for key in key_list:

        letter_range = re.search(range_regex, key).group(0).strip().split('-')
        letter_check = re.search(letter_regex, key).group(0).strip()
        password = re.search(pass_regex, key).group(0).strip()[2:]

        min, max = int(letter_range[0]), int(letter_range[1])
        occurrences = password.count(letter_check)

        if min <= occurrences and occurrences <= max:
            continue
        else:
            invalids.append(password)

    return invalids


if __name__ == '__main__':

    print(checkPass(key_list=key_list)[41])




    
