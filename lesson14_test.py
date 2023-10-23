def first(): # ywxz
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((y <= x) == (x <= w)) and (z or x)):
                        print('xyzw: ',  x, y, z, w)

first()

def second(): # ywzx
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((not x) or y or z) == ((not y) and z and w):
                        print('xyzw: ',  x, y, z, w)

def third(): # yxzw
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (x == (w or y) or ((w <= z) and (y <= w))) == 0:
                        print('xyzw: ',  x, y, z, w)

def fourth(): # 22
    for n in range(1, 1000):
        s = bin(n)[2:]
        if n % 2 == 0:
            s += '00'
        else:
            s += '11'
        if int(s, 2) < 94:
            print(n)

def fifty(): # 1396
    for x in range(1000, 10000):
        n = str(x)
        s1 = int(n[0]) + int(n[1])
        s2 = int(n[1]) + int(n[2])
        s3 = int(n[2]) + int(n[3])
        maxi = str(max(s1, s2, s3))
        avg = str(s1 + s2 + s3 - max(s1,s2,s3) - min(s1,s2,s3))
        if avg + maxi == '1215':
            print(x)
            break

def sixth(): # 402
    for n in range(1, 1000):
        s = bin(n)[2:]
        s += str((s.count('1') % 2))
        s += str((s.count('1') % 2))
        if int(s, 2) > 396:
            print(int(s, 2))
            break

def seventh(): # 2211
    s = '1' * 80
    while '11111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    print(s)

def eight(): # 388
    s = '8' * 125
    while ('333' in s) or ('888' in s):
        if '333' in s:
            s = s.replace('333', '8', 1)
        else:
            s = s.replace('888', '3', 1)
    print(s)

def ninth(): # 211
    s = '1' * 100
    while '111' in s:
        s = s.replace('11', '2', 1)
        s = s.replace('22', '1', 1)
    print(s)

def tenth(): # 10090
    for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        s = int(f'317{x}', 36) + int(f'4{x}29', 36)
        if s % 36 == 0:
            print(s / 36)

def eleventh(): # 36701
    for x in '0123456789ABCDEF':
        s = int(f'8{x}834', 16) + int(f'44{x}27', 16)
        if s % 23 == 0:
            print(s / 23)

def twentith(): # 224
    for x in '01234567890AB':
        s = int(f'2AB{x}', 12) + int(f'{x}8E', 17)
        if s % 27 == 0:
            print(s / 27)

def f1(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    if n > 3:
        return f1(n-3) + f1(n-2)

def threetenth(): # 16
    print(f1(12))

def f2(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * g2(n-1) + 5 * n

def g2(n):
    if n == 1:
        return 1
    if n > 1:
        return f2(n-1) + 2 * n

def fourthtenth(): # 89
    print(f2(4) + g2(4))

def f3(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f3(n-1)
    if n > 1 and n % 2 != 0:
        return 2 * f3(n-2)

def fifthtenth(): # 4122
    print(f3(26))