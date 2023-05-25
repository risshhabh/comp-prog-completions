# http://www.usaco.org/index.php?page=viewproblem2&cpid=1083

alpha, phrase = input(), input()

print(1 + sum(alpha.index(phrase[i]) <= alpha.index(phrase[i - 1]) for i in range(1, len(phrase))))
