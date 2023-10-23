def first(): # 9810
    for i in range(1000, 10000):
        s = str(i)
        c1 = int(s[0]) + int(s[1])
        c2 = int(s[2]) + int(s[3])
        ans = int(str(min(c1, c2)) + str(max(c1, c2)))
        if ans == 117:
            print(i)

def third(): # 9878
    for i in range(1000, 10000):
        s = str(i)
        c1 = int(s[0]) + int(s[1])
        c2 = int(s[1]) + int(s[2])
        c3 = int(s[2]) + int(s[3])
        if max(c1, c2, c3) == c1:
            b = max(c2, c3)
        if max(c1, c2, c3) == c2:
            b = max(c1, c3)
        if max(c1, c2, c3) == c3:
            b = max(c2, c1)
        ans = int(str(b) + str(max(c1, c2, c3)))
        if ans == 1517:
            print(i)

def fourth(): # 9424
    for i in range(1000, 10000):
        s = str(i)
        c1 = int(s[0]) + int(s[1])
        c2 = int(s[1]) + int(s[2])
        c3 = int(s[2]) + int(s[3])
        if max(c1, c2, c3) == c1:
            b = max(c2, c3)
        if max(c1, c2, c3) == c2:
            b = max(c1, c3)
        if max(c1, c2, c3) == c3:
            b = max(c2, c1)
        ans = int(str(b) + str(max(c1, c2, c3)))
        if ans == 613:
            print(i)

def fifth(): # 9696
    for i in range(10000,1000,-1):
        s = str(i)
        c = [0,0,0]
        for j in range(1,4):
            c[j-1] = int(s[j-1]) + int(s[j])
        c.sort(reverse=True)
        r = str(c[1]) + str(c[0])
        if r == "1515":
            print(i)
            break

def sixth(): # 1698
    for i in range(1000, 10000):
        s = str(i)
        c1 = int(s[0]) + int(s[1])
        c2 = int(s[1]) + int(s[2])
        c3 = int(s[2]) + int(s[3])
        if max(c1, c2, c3) == c1:
            b = max(c2, c3)
        if max(c1, c2, c3) == c2:
            b = max(c1, c3)
        if max(c1, c2, c3) == c3:
            b = max(c2, c1)
        ans = int(str(b) + str(max(c1, c2, c3)))
        if ans == 1517:
            print(i)
            break

def seventh(): # 3950
    for i in range(1000,10000):
        s = str(i)
        c = [0, 0]
        for j in range(1, 3):
            c[j - 1] = int(s[j - 1]) + int(s[j])
        r = str(max(c)) + str(min(c))
        if r == "1412":
            print(i)
            break
sixth()