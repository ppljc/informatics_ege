def first():
    for x in '0123456789a':
        for y in '0123456789a':
            r = int(f'{x}341{y}', 11) + int(f'56{x}1{y}', 19)
            if r % 305 == 0:
                print(r // 305)

def second(): # 234
    for x in '0123456789abc':
        r = int(f'4c{x}4', 15) + int(f'{x}62a', 13)
        if r % 121 == 0:
             print(r // 121)

second()