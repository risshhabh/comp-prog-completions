# https://codeforces.com/contest/1829/problem/B

from itertools import groupby

for _ in range(int(input())):
    input()
    a = input().replace(" ", "")
    out = [0]
    for _, g in groupby(a):
        if (b := list(g))[0] == "0": out.append(len(b))

    print(max(out))
