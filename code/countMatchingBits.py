def count_matching_bits(*data):
    result = 0
    for i in range(bin(min(data)).__len__()):
        is_similar = True
        for j in range(data.__len__()):
            is_similar *= (bin(data[0])[i] == bin(data[j])[i])
        if is_similar:
            result += 1
    return result
