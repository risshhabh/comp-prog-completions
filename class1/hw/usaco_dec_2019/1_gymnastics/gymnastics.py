# http://www.usaco.org/index.php?page=viewproblem2&cpid=963
# USACO 2019 December Contest, Bronze
# Problem 1. Cow Gymnastics

gin = open("gymnastics.in", "r")
K, N = map( int, gin.readline().split() )
glines = [ list(map( int, l.split() )) for l in gin.read().splitlines() ]

c = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        consistent = True
        for line in glines:
            if line.index(j) < line.index(i):
                consistent = False  # can convert 16-18 into all
        if consistent: c += 1

gout = open("gymnastics.out", "w")
gout.write(str(c) + "\n")
