def _get_permutations(iterable):
    result = []
    def permute(iterable, start_index, end_index):
        # import pdb
        # pdb.set_trace()
        nonlocal result
        if start_index == end_index:
            result.append([x for x in iterable])
        else:    
            for i in range(start_index, end_index):
                iterable[start_index], iterable[i] = iterable[i], iterable[start_index]
                permute(iterable, start_index + 1, end_index)
                iterable[start_index], iterable[i] = iterable[i], iterable[start_index]

    permute(iterable, 0, len(iterable))
    return result