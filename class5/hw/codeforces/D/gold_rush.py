# https://codeforces.com/contest/1829/problem/D

splint = lambda : list(map(int, input().split()))

def check_recur(n, m):
    # base case
    if m == n:
        return True
    elif m > n or n % 3:
        return False

    return check_recur(n // 3, m) or check_recur(2 * n // 3, m)


for _ in range(int(input())):
    n, m = splint()
    print("YES" if check_recur(n, m) else "NO")
