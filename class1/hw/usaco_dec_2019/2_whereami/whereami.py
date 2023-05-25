# http://www.usaco.org/index.php?page=viewproblem2&cpid=964
# USACO 2019 December Contest, Bronze
# Problem 2. Where Am I?

win = open("whereami.in", "r")
N = int(win.readline())
mailboxes = win.readline()


for K in range(1, N + 1):
    # can use list comp
    wns = []  # All windows of length K
    for w in range(N + 1 - K):
        wns.append(mailboxes[w:w+K])

    if len(set(wns)) == N - K + 1:  # If there are no duplicate windows,
        wout = open("whereami.out", "w")
        wout.write(str(K) + "\n")   # John can identify uniqueness for that K.
        wout.close()
        break
