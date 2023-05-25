# http://www.usaco.org/index.php?page=viewproblem2&cpid=963

K, N = list(map(int, input().split()))

sessions = []
for _ in range(K):
    sessions.append(list(map(int, input().split())))

global consistent 
consistent = True

def check_consistency(diff, i):
    for s in sessions:
        if s.index(i) > s.index(i - diff):
            consistent = False
            diff -= 1

    return diff, i

consistents = []
for i in range(2, N):

    x = check_consistency(1, i)

    if consistent:
        consistents.append((i, i - x[0]))

print(consistents)
