# https://codeforces.com/problemset/problem/1774/A

for _ in range( int(input()) ):
    n = int(input())  # unused
    a = input()

    #      "+"                      "-"
    sign = True if a[0] == "0" else False
    
    for b in a[1:]:
        print("+" if sign else "-", end="")
        sign = not sign if b == "1" else sign
    print()
