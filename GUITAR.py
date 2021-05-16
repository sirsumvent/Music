neck = [['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
        ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
        ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
        ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
        ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
        ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---'],
        [' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10', ' 11', ' 12']]

# neckNote = [['|-e-', '|-F-', '|-F#-', '|-G-', '|-G#-', '|-A-|', '|-A#-', '|-B-', '|-C-', '|-C#-', '|-D-|', '|-D#-', '|-E-|'],
    #         ['|-B-', '|-C-', '|--C#-', '|-D-', '|-D#-', '|-E-|', '|-F-', '|-F#-', '|-G-', '|-G#-', '|-A-|', '|-B-'],
    #         ['|-G-', '|-G#-', '|-A-', '|-A#-', '|-B-', '|-C-|', '|--C#-', '|-D-', '|-D#-', '|-E-|', '|-F-', '|-F#-', '|-G-'],
    #         ['|-D-', '|-D#-', '|-E-', '|-F-', '|-F#-', '|-G-|', '|-G#-', '|-A-|', '|-A#-', '|-B-', '|-C-', '|-C#-', , '|-D-|'],
    #         ['|-A-', '|-A#-', '|-B-', '|-C-', '|-C#-', '|-D-|', '|-D#-', '|-E-', '|-F-', '|-F#-', '|-G-|', '|-G#-', '|-A-|'],
    #         ['|-E-', '|-F-', '|-F#-', '|-G-', '|-G#-', '|-A-|', '|-A#-', '|-B-', '|-C-', '|-C#-', '|-D-|', '|-D#-', '|-E-|']]

cnote = '-C-'
csharp = '-c#'
dnote = '-D-'
dsharp = '-D#'
enote = '-E-'
fnote = '-F-'
fsharp = '-F#'
gnote = '-G-'
gsharp = '-G#'
anote = '-A-'
asharp = '-A#-'
bnote = '-B-'

print('Once you are done, type "stop"')
print()
print()

while True:
    looking = input('What note are you looking for?').casefold()
    # looking for a particular note:
    if looking == 'c':
        looking = [4, 3, 1, 1, 2, 5, 0, 8, 3, 10, 5, 8]  # coordinates (x, y) values
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]   # index for x value
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]  # index for y value
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)] = cnote, cnote, cnote, cnote, cnote, cnote, # '-C-', '-C-', '-C-', '-C-', '-C-', '-C-'


    if looking == 'c#':
        looking = [4, 4, 1, 2, 0, 9, 2, 6, 3, 11, 5, 9]  # coordinates (x, y) values
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)] = csharp, csharp, csharp, csharp, csharp, csharp,

    if looking == 'd':
        looking = [3, 0, 1, 3, 4, 5, 2, 7, 0, 10, 5, 10]
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)] = dnote, dnote, dnote, dnote, dnote, dnote,

    if looking == 'd#':
        looking = [3, 1, 1, 4, 4, 6, 2, 8, 0, 11, 5, 11]  # coordinates (x, y) values
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)] = dsharp, dsharp, dsharp, dsharp, dsharp, dsharp,

    if looking == 'e':
        looking = [0, 0, 1, 5, 5, 0, 3, 2, 4, 7, 0, 12, 5, 12, 2, 9]
        x1, x2, x3, x4, x5, x6, x7, x8 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10], looking[12], looking[14]
        y1, y2, y3, y4, y5, y6, y7, y8 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11], looking[13], looking[15]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)], \
        neck[int(x7)][int(y7)], neck[int(x8)][int(y8)] = '-e-', enote, enote, enote, enote, enote, enote, enote,

    if looking == 'f':
        looking = [0, 1, 3, 3, 5, 1, 1, 6, 4, 8, 2, 10]
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)] = fnote, fnote, fnote, fnote, fnote, fnote,

    if looking == 'f#':
        looking = [0, 2, 3, 4, 5, 2, 1, 7, 4, 9, 2, 11]
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)] = fsharp, fsharp, fsharp, fsharp, fsharp, fsharp

    if looking == 'g':
        looking = [0, 3, 3, 5, 5, 3, 1, 8, 4, 10, 2, 0, 2, 12]
        x1, x2, x3, x4, x5, x6, x7 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10], looking[12]
        y1, y2, y3, y4, y5, y6, y7 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11], looking[13]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)], \
        neck[int(x7)][int(y7)] = gnote, gnote, gnote, gnote, gnote, gnote, gnote,

    if looking == 'g#':
        looking = [0, 4, 3, 6, 5, 4, 1, 9, 4, 11, 2, 1]
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)] = gsharp, gsharp, gsharp, gsharp, gsharp, gsharp,

    if looking == 'a':
        looking = [0, 5, 2, 2, 4, 0, 5, 5, 3, 7, 1, 11, 4, 12]
        x1, x2, x3, x4, x5, x6, x7 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10], looking[12]
        y1, y2, y3, y4, y5, y6, y7 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11], looking[13]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)], \
        neck[int(x7)][int(y7)] = anote, anote, anote, anote, anote, anote, anote,

    if looking == 'a#':
        looking = [0, 6, 2, 3, 4, 1, 5, 6, 3, 8, 1, 12]
        x1, x2, x3, x4, x5, x6 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10]
        y1, y2, y3, y4, y5, y6 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)], \
        neck[int(x3)][int(y3)], neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)], = asharp, asharp, asharp, asharp, asharp, asharp,

    if looking == 'b':
        looking = [1, 0, 2, 4, 4, 2, 0, 7, 5, 7, 1, 12, 3, 9]  # coordinates (x, y) values
        x1, x2, x3, x4, x5, x6, x7 = looking[0], looking[2], looking[4], looking[6], looking[8], looking[10], looking[12]
        y1, y2, y3, y4, y5, y6, y7 = looking[1], looking[3], looking[5], looking[7], looking[9], looking[11], looking[13]
        # find x,y values and replace with ' '
        neck[int(x1)][int(y1)], neck[int(x2)][int(y2)],\
        neck[int(x3)][int(y3)],neck[int(x4)][int(y4)], \
        neck[int(x5)][int(y5)], neck[int(x6)][int(y6)], \
        neck[int(x7)][int(y7)] = bnote, bnote, bnote, bnote, bnote, bnote, bnote,

    # to exit the loop
    if looking == 'stop':
        break

frets = input('How many frets?')
# create the matrix blank, if no values, or with 'looking' parameters
for x in range(7):
    for y in range(int(frets)):
        if y == 0:
            print('|' + neck[x][y], end='|')
        else:
            print(neck[x][y], end='|')
    print()
