def first(): # zwyx
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((x and y) <= ((not z) or w)) and (((not w) <= x) or (not y))) == 0:
                        print('xyzw: ', x, y, z, w)

def third():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((not z) == y) <= ((w and (not x)) == (y and x))) == 0:
                        print('xyzw: ', x, y, z, w)

def fifty():
    f = 0
    for n in range(120000000, 1000000000):
        s = bin(n)[2:]
        if s.count('1') % 2 == 0:
            s += '000'
        if s.count('1') % 2 != 0:
            s += '100'
        r = int(s, 2)
        print(r)
        if (r >= 987654321) and (r <= 2123456789):
            f += 1
            print(f)
        if r == 2123456789:
            break
    print('Result: ', f)

def seventh(): # 345
    for x in '0123456789ABCDEF':
        r = int(f'2{x}84', 19) + int(f'2B3{x}', 16)
        if r % 88 == 0:
            print(r // 88)

def ninth(): # 45963
    for x in '0123456789ABCDEF':
        r = int(f'8{x}84{x}', 16) + int(f'78{x}34', 16)
        if r % 23 == 0:
            print(r // 23)

def f10(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f10(n - 1)
    if (n > 1) and (n % 2 != 0):
        return 2 * f10(n - 2)

def tenth(): # 4122
    print(f10(26))

def f11(n):
    if (n == 1) or (n == 2):
        return 1
    if n > 2:
        return f11(n - 2) * (n + 1)

def eleventh(): # 315
    print(f11(8))

fifty()
