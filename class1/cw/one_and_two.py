# https://codeforces.com/problemset/problem/1788/A

outputs = int(input())
# for _ in range(int(input())):

for inp in range(outputs):

    out = -1

    n = int(input())
    lst = [int(i) for i in input().split()]  # use map

    # find k
    for k in range(1, n):
        left = lst[0:k]  # list splicing is slow
        right = lst[k:]
        
        prod = 1
        for l in left:
            prod *= l
        for r in right:
            prod = prod / r
        
        if prod == 1:
            out = k
            break

    print(out)
