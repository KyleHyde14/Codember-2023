def decode():
    message = input('Choose a message to decode: ')

    try:
        str(message)
    except:
        return 'The message must be a string'

    message_cleaned  = message.lower().split()

    dic = {}

    answer = ''

    for _ in message_cleaned:
        if _ in dic:
            dic[_] += 1
        
        else:
            dic[_] = 1

    for k,v in dic.items():
        answer += k + str(v)

    return 'Decoded message is: \n' + answer

if __name__ == '__main__':
    print(decode())