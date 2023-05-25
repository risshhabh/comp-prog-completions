# A : Plus or Minus
# https://codeforces.com/contest/1807/problem/A

print( "\n".join([ "+" if sum( ( s := list(map( int, input().split() )) )[:2] ) == s[-1] else "-" for _ in range( int(input()) ) ]) )


# If sum of first two elements == last element, "+"
# Else, "-"
# Make list out of this
# Print this list with "\n" split
