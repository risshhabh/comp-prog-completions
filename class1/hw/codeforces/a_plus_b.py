# https://codeforces.com/problemset/problem/1772/A

for _ in range( int(input()) ):
    print(
        sum(
            list(map( int, input().split("+") ))
        )
    )
