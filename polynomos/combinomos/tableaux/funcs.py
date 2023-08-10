from polynomos.lists.plainlist import PlainList

def ferrers_diagram(partition: PlainList, notation: str, character: str):
    if notation == 'french':
        for i in range(1, len(partition)):
            if partition[i] < partition[i - 1]:
                raise ValueError("Given list must be sorted in ascending order")
    else:
        for i in range(1, len(partition)):
            if partition[i] > partition[i - 1]:
                raise ValueError("Given list must be sorted in descending order")
    ferrer_strs = []
    for part in partition:
        ferrer_strs.append(' '.join([character] * part))

    return '\n'.join(ferrer_strs)

def partition_transpose(partition):
    s = [x for x in partition if x > 0] + [0]
    result = []
    idx = 1
    first = s[0]

    while first > 0:
        while first > s[idx]:
            result.insert(0, idx)
            first -= 1
        idx += 1

    return PlainList(*result)

def durfee_square(partition):
    if len(partition) == 0:
        return 0
    max_square = 1
    for i in range(1, min(len(partition), partition[0])):
        if partition[i] >= i + 1:
            max_square = i + 1

    return max_square