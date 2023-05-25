# D. Distinct Split
# https://codeforces.com/contest/1791/problem/D

for _ in range(int(input())):
    n = int(input())
    s = input()

    prefixes = []
    suffixes = []
    
    prefix, suffix = set(), set()
    for i in range(n - 1):
        prefix.add(s[i])
        suffix.add(s[n - i - 1])
        prefixes.append(len(prefix))
        suffixes.append(len(suffix))
    suffixes = suffixes[::-1]

    maximum = max(a + b for a, b in zip(prefixes, suffixes))

    print(maximum)

