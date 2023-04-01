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

