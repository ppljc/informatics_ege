def first(): # 46
    for n in range(1, 1000):
        x = bin(n)[2:]
        if x.count('1') % 2 == 0:
            x += '00'
        else:
            x += '10'
        if int(x, 2) > 43:
            print(int(x, 2))
            break

def second(): # 115
    for n in range(1, 1000):
        x = bin(n)[2:]
        if x.count('1') % 2 == 0:
            x += '00'
        else:
            x += '11'
        if int(x, 2) > 114:
            print(int(x, 2))
            break

def third(): # 111
    for n in range(1, 1000):
        x = bin(n)[2:]
        s = str(x)
        s += s[-1]
        s += str(s.count('1')%2)
        if int(s, 2) > 105:
            print(int(s, 2))
            break


def fourth():
    for n in range(1,10000):
        x = bin(n)[2:]
        s = int(x) // 10
        s = str(s)
        if n % 2 == 0:
            s += "01"
        else:
            s += "10"
        if int(s, 2) == 2018:
            print(n)
            break

fourth()