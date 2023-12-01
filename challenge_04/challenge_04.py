with open('s4vitar.txt', 'r') as file:
    stolen = []

    for line in file:
        stolen.append(line[:-1])

def analyze(array):
    ans = []
    for i in array:
        alpha, possible_checksum = i.split('-')

        if all(alpha.count(x) == 1 for x in possible_checksum):
            ans.append(possible_checksum)

    return ans


if __name__ == '__main__':
    print(analyze(stolen)[32])
