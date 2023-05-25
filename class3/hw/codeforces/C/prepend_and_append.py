# C. Prepend and Append
# https://codeforces.com/contest/1791/problem/C

for _ in range(int(input())):
    out = int(input())
    s = input()

    while s[0] != s[-1]:
        s = s[1:-1]  # O(n)
        out -= 2
        if len(s) <= 1:
            break

    print(out)
