def first(n, x, type):
    s = [0, 0, 0]
    for i in range(1, n):
        s = [i + 1, i + 2, i * 2]
        for turns in range(1, x):
            for o in range(3):
                if type == 'or' and (s[o] + 1 >= n or s[o] + 2 >= n or s[o] * 2 >= n):
                    print(i-1)
                    return
                if type == 'and' and (s[o] + 1 >= n and s[o] + 2 >= n and s[o] * 2 >= n):
                    print(i-1)
                    return
            if x > 2:
                s = [i + 1, i + 2, i * 2]

first(34, 3, 'or')
