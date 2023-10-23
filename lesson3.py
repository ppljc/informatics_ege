# def func():
#     a = 1267
#     b = bin(a)[2:]
#     c = oct(a)[2:]
#     d = hex(a)[2:]
#
#     digits = '0123456789abcdefghijklmnoprstyvwxyz'

def first(): # 9
    x = (343**6)-(7**10)+47
    ans = ''
    while x!=0:
        ans += str(x % 7)
        x //= 7
    ans = ans[::-1]
    print(ans.count('6'))

def second(): # 21
    x = (4 ** 12) + (2 ** 32) - 16
    ans = ''
    while x != 0:
        ans += str(x % 2)
        x //= 2
    ans = ans[::-1]
    print(ans.count('1'))

def third(): # 151
    x = 7*(512**120) - 6*(64**100) + 8**210 - 255
    ans = ''
    while x != 0:
        ans += str(x % 8)
        x //= 8
    ans = ans[::-1]
    print(ans.count('0'))

def fourth(): # 3
    x = 9**8 + 3**5 - 9
    ans = ''
    while x != 0:
        ans += str(x % 3)
        x //= 3
    ans = ans[::-1]
    print(ans.count('2'))

fourth()