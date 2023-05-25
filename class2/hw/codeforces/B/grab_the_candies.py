# B : Grab the Candies
# https://codeforces.com/contest/1807/problem/B

from random import getrandbits

# "You can output the answer in any case"
def randcase(st: str):
    return "".join([ st[ch].upper() if [getrandbits(1) for _ in range(len(st))][ch] else st[ch].lower() for ch in range(len(st)) ])

# Start if-statement is workaround to use walrus operator
print("\n".join([ ("" if (u := input()) else "") + ("" if (candies := list(map(int, input().split()))) == None else "") + ( randcase("YES") if sum( even for even in candies if not even % 2 ) > sum( odd for odd in candies if odd % 2 ) else randcase("NO") ) for _ in range(int(input())) ]))
