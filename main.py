from string import hexdigits
from functools import partial
from math import hypot

int16 = partial(int, base=16)

colors =   {'ffffff': 'neutrals-white',
            'fafafa': 'neutrals-lightest',
            'eff0f3': 'neutrals-lighter',
            }

def isvalid(hex_hey):
    return len(hex_key) == 6 and all(ch in hexdigits for ch in hex_key)

def hex_to_tup(s):
    split = s[:2], s[2:4], s[4:]
    return tuple(map(int16, split))

def tup_to_hex(tup):
    return ''.join(f'{i:x}' for i in tup)

def dist(tup1, tup2):
    diff = tuple(a - b for a, b in zip(tup1, tup2))
    return hypot(*diff)

def get_match(hex_key):
    col_val = hex_to_tup(hex_key)
    search = lambda x: dist(x, col_val)
    nearest = min(map(hex_to_tup, colors.keys()), key=search)
    return colors[tup_to_hex(nearest)]

bot_status = True
while bot_status is True:
    while True:
        hex_key = input('Enter hex value: ').strip().lower()
        if isvalid(hex_key):
            break
        print('Invalid input, try again.')

    try:
        col_name = colors[hex_key]
        found = True
    except KeyError:
        col_name = get_match(hex_key)
        found = False

    if found:
        print('Colour is in palette:')
    else:
        print('Colour not in palette, nearest match found is:')

    print(col_name)