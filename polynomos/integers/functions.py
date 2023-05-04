def extended_euclidean(a: int, b: int):
    old_s, s = 1, 0
    old_r, r = a, b

    while r != 0:
        quot = old_r // r
        old_r, r = r, old_r - quot * r
        old_s, s = s, old_s - quot * s

    if b != 0:
        x = (old_r - old_s * a) // b
    else:
        x = 0

    return (old_r, old_s, x)

def gcd(a: int, b: int):
    if b > a:
        a, b = b, a

    if b == 0:
        return a
    
    return gcd(b, a % b)

def partition_integer(n: int):
    try:
        if n <= 0:
            return PlainList(PlainList())
        end_list = PlainList()
        current_partition = PlainList(*([0] * n))
    except NameError:
        from polynomos.lists.plainlist import PlainList
        if n <= 0:
            return PlainList(PlainList())
        end_list = PlainList()
        current_partition = PlainList(*([0] * n))

    k = 0
    current_partition[k] = n
    
    while True:
        end_list = end_list.append(PlainList(*[x for x in current_partition._list[:k + 1] if x > 0]))
        
        remainder = 0

        while k >= 0 and current_partition[k] == 1:
            remainder += current_partition[k]
            k -= 1

        if k < 0:
            return end_list
        
        current_partition[k] -= 1
        remainder += 1
        
        while remainder > current_partition[k]:
            current_partition[k + 1] = current_partition[k]
            remainder -= current_partition[k]
            k += 1

        current_partition[k + 1] = remainder
        k += 1