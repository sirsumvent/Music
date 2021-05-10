neck = [['|---', '|---', '|---', '|---', '|---', '|---|'],
        ['|---', '|---', '|---', '|---', '|---', '|---|'],
        ['|---', '|---', '|---', '|---', '|---', '|---|'],
        ['|---', '|---', '|---', '|---', '|---', '|---|'],
        ['|---', '|---', '|---', '|---', '|---', '|---|'],
        ['|---', '|---', '|---', '|---', '|---', '|---|'],
        ['| 0 ', '| 1 ', '| 2 ', '| 3 ', '| 4 ', '| 5 |']]

# neckNote = [['|-e-', '|-F-', '|-F#-', '|-G-', '|-G#-', '|-A-|'],
#         ['|-B-', '|-C-', '|--C#-', '|-D-', '|-D#-', '|-E-|'],
#         ['|-G-', '|-G#-', '|-A-', '|-A#-', '|-B-', '|-C-|'],
#         ['|-D-', '|-D#-', '|-E-', '|-F-', '|-F#-', '|-G-|'],
#         ['|-A-', '|-A#-', '|-B-', '|-C-', '|-C#-', '|-D-|'],
#         ['|-E-', '|-F-', '|-F#-', '|-G-', '|-G#-', '|-A-|']]

looking = input('What note are you looking for?')

# create a blank fretboard
# for x in range(6):
#     for y in range(6):
#         print(neck[x][y], end='')
#     print()

# looking for a particular note:
if looking == 'C'.casefold():
    looking = '4, 3, 1, 1, 2, 5'  # coordinates (x, y) values
    x1, x2, x3 = looking[0], looking[6], looking[12] # index for x value
    y1, y2, y3 = looking[3], looking[9], looking[15] # index for y value
    # find x,y values and replace with ' '
    neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], neck[int(x3)][int(y3)] = '|-C-', '|-C-', '|-C-|'  # fin
    # newNeck = 'neck[{0}][{1}]'.format(looking[0], looking[3])


if looking == 'D'.casefold():
    looking = '3, 0, 1, 3, 4, 5'
    x1, x2, x3 = looking[0], looking[6], looking[12]  # index for x value
    y1, y2, y3 = looking[3], looking[9], looking[15]  # index for y value
    # find x,y values and replace with ' '
    neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], neck[int(x3)][int(y3)] = '|-D-', '|-D-', '|-D-|'


# create the matrix blank, if no values, or with 'looking' parameters
for x in range(7):
    for y in range(6):
        print(neck[x][y], end='')
    print()



