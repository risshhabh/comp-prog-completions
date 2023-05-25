# https://codeforces.com/contest/1742/problem/E

splint = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, q = splint()
    A = splint()
    K = splint()

    out = []

    for k in K:
        broken = False
        for i in range(n):
            if A[i] > k:
                out.append(str(sum(A[:i])))
                broken = True
                break
        if not broken:
            out.append(sum(A))


    print(*out)

