def first(): # 262
    for x in '01234567':
        for y in '01234567':
            r = int(f'{x}01{y}4', 9) + int(f'{x}{y}544', 8)
            if r % 89 == 0:
                print(r // 89)

def second(): # 10
    x = 125**4 + 25**8 - 30
    ans = ''
    while x != 0:
        ans += str(x % 5)
        x //= 5
    ans = ans[::-1]
    print(ans.count('4'))

def third(): # 15374
    for x in '0123456789abcd':
        r = int(f'1{x}563', 14) + int(f'871{x}3', 14)
        if r % 24 == 0:
            print(r // 24)

def fourth(): # 345
    for x in "0123456789ABCDEF":
        r = int(f"2{x}84", 19) + int(f"2B3{x}", 16)
        if r % 88 == 0:
            print(r // 88)

def fifth(): # 9
    x = 48**8 + 7**24 - 7
    ans = ''
    while x!=0:
        ans += str(x%7)
        x //= 7
    ans = ans[::-1]
    print(ans.count('0'))

def sixth(): # 169
    for x in '012345678':
        for y in '012345678':
            r = int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)
            if r % 170 == 0:
                print(r // 170)

sixth()
