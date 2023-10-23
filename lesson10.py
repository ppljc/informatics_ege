import sys
sys.setrecursionlimit(10**8)

def first(): # 220
    for n in range(128, 256):
        s = bin(n)[2:]
        s1 = ''
        for i in s:
            if i == '1':
                s1 += '0'
            if i == '0':
                s1 += '1'
        s2 = int(s1, 2)
        if n-s2 == 185:
            print(n)

def second(): # 9424
    for n in range(10000, 1000, -1):
        n = str(n)
        r1 = int(n[0]) + int(n[1])
        r2 = int(n[1]) + int(n[2])
        r3 = int(n[2]) + int(n[3])
        arr = [r1,r2,r3]
        arr.sort(reverse=True)
        r = str(arr[1]) + str(arr[0])
        if r == "613":
            print(n)
            break

def third():
    f = 0
    for n in range(10000000, 1000000000):
        s = bin(n)[2:]
        if s.count('1') % 2 == 0:
            s += '000'
        if s.count('1') % 2 != 0:
            s += '100'
        r = int(s, 2)
        if (r >= 123456789) and (r <= 1987654321):
            f += 1
        if r == 1987654321:
            break
    print(f)

def fourth():
    for i in range(100, 1000):
        r1 = str(i[0]) + str(i[1])
        r2 = str(i[1]) + str(i[2])
        if max(r1, r2) == r1:
            print()

third()