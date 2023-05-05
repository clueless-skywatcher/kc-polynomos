def ferrers_diagram(l, notation, character):
    if notation == 'french':
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                raise ValueError("Given list must be sorted in ascending order")
    else:
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                raise ValueError("Given list must be sorted in descending order")
    ferrer_strs = []
    for part in l:
        ferrer_strs.append(' '.join([character] * part))

    return '\n'.join(ferrer_strs)