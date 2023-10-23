import sys
sys.setrecursionlimit(10**8)

def first():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((w<=x) and ((y<=z) == (x<=y))):
                        print('xyzw: ', x, y, z, w)

def second():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x and y and (not z)) == (y or  z or (not w))):
                        print('xyzw: ', x, y, z, w)

def third():
    for x in "0123456789a":
        r = int(f"982{x}8", 11) + int(f"194{x}7", 11)
        if r % 58 == 0:
            print(r // 58)


def fourth():
    print(bin((8**7)+(4**5)+(2**10)-32)[2:])
    print(bin((8**7)+(4**5)+(2**10)-32)[2:].count("1"))

def fifth():
    for x in '012345678':
        for y in '012345678':
            r = int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)
            if r % 170 == 0:
                print(r//170)

def sixth():
    for x in '0123456789a':
        r = int(f'95{x}2', 11) + int(f'{x}458', 12)
        if r % 136 == 0:
            print(r//136)


def seventh():
    for x in "0123456789AB":
        M = int(f"49{x}26", 12)
        N = int(f"49{x}70", 12)
        for A in range(100):
            if (M + A) % N == 0:
                print(A, x)
                break

def eigth():
    a = (343**5) - (7**9) + 48
    r = ""
    while a != 0:
        r += str(a % 7)
        a //= 7
    r = r[::-1]
    print(r)
    print(r.count("6"))

def f1(n):
    if n>=11:
        return n+f1(n-1)
    if n<11:
        return 10

def nineth():
    print(f1(2124)-f1(2122))

nineth()