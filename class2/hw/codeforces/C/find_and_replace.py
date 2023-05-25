# C : Find and Replace
# https://codeforces.com/contest/1807/problem/C

ind_find = lambda char, strn : [i for i, c in enumerate(strn) if c == char]
ind_diff = lambda ind_list   : [ind_list[i] - ind_list[i - 1] for i in range(1, len(ind_list))]

for _ in range(int(input())):  # <=100
    input()
    out = "YES"
    for char in set((s := input())):
        if sum([1 for d in ind_diff(ind_find(char, s)) if d % 2]):
            out = "NO"
    print(out)
