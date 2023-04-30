def _get_permutations(iterable):
    result = []
    def permute(iterable, start_index, end_index):
        nonlocal result
        if start_index == end_index:
            result.append([x for x in iterable])
        else:    
            for i in range(start_index, end_index):
                iterable[start_index], iterable[i] = iterable[i], iterable[start_index]
                permute(iterable, start_index + 1, end_index)
                iterable[start_index], iterable[i] = iterable[i], iterable[start_index]

    permute(iterable, 0, len(iterable))
    return sorted(result)

def _get_combinations(iterable, k):
    result = []
    n = len(iterable)
    if k > n:
        return result
    
    indices = list(range(k))
    result.append([iterable[i] for i in indices])
    while True:
        for i in reversed(range(k)):
            if indices[i] != i + n - k:
                break
        else:
            return result
        indices[i] += 1
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1
        result.append([iterable[i] for i in indices])
