# D : Odd Queries
# https://codeforces.com/contest/1807/problem/D

splinput = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, q = splinput()
    a = list(map(lambda x : int(x) % 2, input().split()))

    prefix, ct = [0], 0
    for i in range(n):
        ct += a[i]
        prefix.append(ct)

    for _ in range(q):
        l, r, k = splinput()
        sumlr = k * (r - l + 1) 
        newsum = ct - sumlr + prefix[r] - prefix[l - 1]
        
        if newsum % 2:
            print("YES")
        else: print("NO")

