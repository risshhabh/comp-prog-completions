# len of the powerset is 2^len(l)
def powerset(l: list):

    if len(l) == 0:
        return [[]]

    out = []
    x = l.pop()
    for p in powerset(l):
        out.append(p)
        out.append(p + [x])

    return out
