# https://codeforces.com/problemset/problem/1672/A

for _ in range(int(input())):
    n = int(input())

    log_sum = sum(map(int, input().split())) - n

    if log_sum % 2:
        print("errorgorn")
    else:
        print("maomao90")
