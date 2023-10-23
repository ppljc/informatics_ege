def first(): # 96
    for n in range(1, 1000):
        s = bin(n)[2:]
        s += f"{s.count('1') % 2}"
        s += f"{s.count('1') % 2}"
        if int(s, 2) < 100:
            print(int(s, 2))

def second(): # 21
    for n in range(1,1000):
        b = bin(n)[2:]
        x1 = str(b.count("1") % 2)
        b += x1
        x2 = str(b.count("1") % 2)
        b += x2
        if int(b,2) > 85:
            print(n)
            break

def third(): # 23
    for n in range(2, 1000):
        s = bin(n)[2:]
        x = s + s[1] + s[0]
        if int(x, 2) > 90:
            print(n)
            break

def fourth(): # 101
    for n in range(10000, 1, -1):
        b = bin(n)[2:]
        if n % 2 == 0:
            b += "10"
        else:
            b += "01"
        if int(b,2) <= 102:
            print(int(b,2))
            break

fourth()