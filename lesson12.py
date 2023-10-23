def first():
    for i in range(1, 1000):
        s = '1' * 10 + '2' * i
        while '19' in s:
            s = s.replace('12', '4', 1)
        if s.count('1') + (s.count('2') * 2) + (s.count('4') * 4) == 25:
            print(i)
            break

def second():
    s = '2' + '9' * 100
    while ('19' in s) or ('299' in s) or ('3999' in s):
        s = s.replace('19', '2', 1)
        s = s.replace('299', '3', 1)
        s = s.replace('3999', '1', 1)
    print(s)