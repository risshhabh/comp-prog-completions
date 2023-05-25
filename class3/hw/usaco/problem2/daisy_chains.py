# Problem 2 : Daisy Chains
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1060

from itertools import combinations
splinput = lambda : list(map(int, input().split()))

out = int(input())
p = splinput()

inds = combinations(range(out), 2)  # O(N^2)

for i in inds:
    wn = p[i[0]:(i[1] + 1)]  # O(N)
    if sum(wn) / (i[1] - i[0] + 1) in wn:
        out += 1

print(out)
