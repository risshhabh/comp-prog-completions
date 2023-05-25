# G1. Teleporters (Easy)
# https://codeforces.com/contest/1791/problem/G1

splinput = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, c = splinput()

    a = [splinput()[i] + i for i in range(n)]
    print(a)
    pos, out = 0, 0
    # while True:
    #     if c < 



    # a = [0] + splinput()
    #
    # # real prices to get there
    # a = [a[i] + i for i in range(n + 1)]
    # a.sort()
    #
    # out = 0
    # while c >= a[out + 1]:
    #     c -= a[out + 1]
    #     out += 1
    #     if out == n:
    #         break
    #
    # print(out)
