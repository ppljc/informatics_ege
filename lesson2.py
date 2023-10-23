def first():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x == (not y)) <= ((x and w) == (z and (not w)))) == 0:
                        print('xyzw: ', x, y, z, w)


def second():
    print("x y z w")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x and not y) or (x == z) or w) == 0:
                        print(x, y, z, w)


def third():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((y<=z) and (not((y or w) <= (z and x)))):
                        print('xyzw: ', x, y, z, w)

def f1(n):
    if n <= 2:
        return n+1
    if n > 2:
        return f1(n-1)*f1(n-2)

def f2(n):
    if n == 1:
        return 1
    elif n > 1:
        return f2(n-1) + (2**(n-1))


def f3(n):
    if n <=2:
        return 1
    elif n > 2:
        return f3(n-1) + (2 * f3(n-2))

print(f3(7))