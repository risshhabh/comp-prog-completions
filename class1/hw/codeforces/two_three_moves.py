# https://codeforces.com/problemset/problem/1716/A

for _ in range( int(input()) ):
    n = int(input())
    print(2 if n == 1 else (n // 3 + (1 if n % 3 != 0 else 0)))

def old():
    for _ in range( int(input()) ):
        n = int(input())
        mins = 0
        
        mins += n // 6 * 2
        if n == 1:
            mins = 2
        elif n % 6 in (4, 5):
            mins += 2
        elif n % 6 in (1, 2, 3):
            mins += 1
        
        print(mins)

