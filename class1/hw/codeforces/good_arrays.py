
#https://codeforces.com/problemset/problem/1777/A
for _ in range( int(input()) ):
    n = int(input())
    a = list(map( lambda x : int(x) % 2, input().split() ))

    operations = 0
    for i in range(0, n - 1):
        if a[i] == a[i + 1]:
            operations += 1

    print(operations)
