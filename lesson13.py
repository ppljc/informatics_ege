def first(): # 152 №6
    s = '1' + '0' * 75
    while ('10' in s) or ('1' in s):
        if '10' in s:
            s = s.replace('10', '001', 1)
        else:
            s = s.replace('1', '00', 1)
    print(s.count('0'))

def second(): # 881 №7
    s = '1' * 100
    while ('111' in s) or ('88888' in s):
        s = s.replace('111', '88', 1)
        s = s.replace('88888', '8', 1)
    print(s)

def third(): # 222111 №8
    s = '1' * 84
    while '11111' in s:
        s = s.replace('222', '1', 1)
        s = s.replace('111', '2', 1)
    print(s)

def fourth(): # 21 №9
    s = '1' * 99
    while '111' in s:
        s = s.replace('11', '2', 1)
        s = s.replace('22', '1', 1)
    print(s)

def fifth(): # 93 №10
    s = '3' * 68
    while ('999' in s) or ('333' in s):
        if '333' in s:
            s = s.replace('333', '9', 1)
        else:
            s = s.replace('999', '3', 1)
    print(s)

fifth()