from math import gcd

def coprime(i, j):
    return gcd(i, j) == 1

splint = lambda : set(map(int, input().split()))

# max 1000^2 * 10

for _ in range(int(input())):
    n = int(input())
    a = splint()

    ixs = {}
    for i, e in enumerate(a):
        if e not in ixs:
            ixs[e] = [i]
        else:
            ixs[e].append(i)

    max_out = -1

    for i in (iks := list(ixs.keys())):
        for j in iks:
            if coprime(i, j):
                max_out = max(max_out, (max(ixs[i]) + max(ixs[j])))

    print(max_out)

    # iteration won't work because O(N^2)
