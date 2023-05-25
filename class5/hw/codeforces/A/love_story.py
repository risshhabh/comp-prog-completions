# https://codeforces.com/contest/1829/problem/A

cf = [99, 111, 100, 101, 102, 111, 114, 99, 101, 115]

for i in range(int(input())):
    n = list(map(ord, input()))
    print(10 - [cf[i] - n[i] for i in range(10)].count(0))
