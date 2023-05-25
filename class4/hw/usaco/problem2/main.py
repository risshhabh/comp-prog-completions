N = int(input())
a = list(map(lambda x : int(x) % 2, input().split()))
 
e = a.count(0)
o = N - e

if e >= o:
    print(2 * o + 1)
else:
    print(2 * e + 2 * (o - e) // 3 + (1 if (o % 3) == 2 else 0))


    # 0 1 1 1 1 1 1 1
    # 0 1 0   1 0   1
    # 1 1 1 1 1 1 1
    # 0   1 0   1
    
    # 1 1 1 1 1 1 1
    # 0   1 0   1 <
    # 0   

    # 5 odds -- 3 evens
    # 6,  -- 2 odds
