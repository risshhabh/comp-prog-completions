# F. Range Update Point Query
# https://codeforces.com/contest/1791/problem/F

splinput = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, q = splinput()
    a = splinput()
    
    for _ in range(q):
        query = input().split()
        
        if query[0] == "1":
            ...
