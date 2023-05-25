# https://codeforces.com/problemset/problem/1772/B

for _ in range( int(input()) ):
    matrix = list(map( int, input().split() )) + list(map( int, input().split() ))[::-1]

    bounds = (
        (0, 2), (1, 3), (2, 0), (3, 1)
    )

    beautiful = False
    for b in bounds:
        if ( matrix[b[0]], matrix[b[1]] ) == ( max(matrix), min(matrix) ):
            beautiful = True
            break

    print("YES") if beautiful else print("NO")

