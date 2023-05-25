# E. Negatives and Positives
# https://codeforces.com/contest/1791/problem/E

splinput = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = splinput()
    negs = sum(1 for i in a if i < 0) % 2
    abssum = [abs(x) for x in a]
    abssum = sum(abssum) - 2 * negs * min(abssum)

    print(abssum)

