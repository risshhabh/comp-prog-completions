# B. Following Directions
# https://codeforces.com/contest/1791/problem/B

for _ in range(int(input())):
    input()
    coords = [0, 0]
    out = "NO"
    for l in input():
        if   l == "U": coords[1] += 1
        elif l == "D": coords[1] -= 1
        elif l == "R": coords[0] += 1
        else         : coords[0] -= 1
        
        if coords == [1, 1]:
            out = "YES"

    print(out)
