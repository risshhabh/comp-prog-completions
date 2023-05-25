# http://www.usaco.org/index.php?page=viewproblem2&cpid=1228

N = int(input())
opers = []
nums = []

for _ in range(N):
    oper, num = input().split()
    opers.append(oper)
    num = int(num)
    nums.append(num)

    for p in range(N):
        # 3 15 47 89
        if opers[p] == "L":...
