# This function just counts the number of matching bits amongst passed bytes
# If bytes has different length in binary representation,
# than the number of compared bits is equal to a length of the shortest byte


def do(*data):
    maxlen = len(bin(max(data))[2:])
    data = [bin(e)[2:] for e in data]
    for i in range(len(data)):
        while len(data[i]) < maxlen:
            data[i] = '0' + data[i]

    result = 0
    for i in range(len(data[0])):   # take an index for a bit
        is_similar = True
        for j in range(len(data)):  # iterate over bytes in data
            is_similar *= (data[0][i] == data[j][i])
        if is_similar:
            result += 1
    return result
