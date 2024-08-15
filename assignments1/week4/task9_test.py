kb = [ ["abcdefghijklm",
       "nopqrstuvwxyz"],

    ["789",
        "456",
        "123",
        "0.-"],

    ["chunk",
        "vibex",
        "gymps",
        "fjord",
        "waltz"],

    ["bemix",
        "vozhd",
        "grypt",
        "clunk",
        "waqfs"]]

def sround_distance(pos1, pos2, length):
    direct = abs(pos1 - pos2)
    sround = length - direct
    return min(sround, direct),sround

def move(x0, y0, x1, y1, i):
    keyboard = kb[i]
    num_row = len(keyboard)
    num_col = len(keyboard[0])

    y_distance, y_sround = sround_distance(y0, y1, num_col)
    x_distance, x_sround = sround_distance(x0, x1, num_row)

    #print('x0:', x0, 'y0:', y0, 'x1:', x1, 'y1:', y1)
    #print('y_dis:', y_distance, 'x_dis:', x_distance)

    if y0 != y1:
        if y_distance == abs(y1 - y0) and y_distance != y_sround:  # No wrapping
            if y1 < y0:
                moves[i].append('l' * y_distance)
            else:
                moves[i].append('r' * y_distance)
        else:  # Wrapping
            if y1 < y0:
                moves[i].append('r' * y_distance + 'w')
            else:
                moves[i].append('l' * y_distance + 'w')

    if x0 != x1:
        if x_distance == abs(x1 - x0) and x_distance != x_sround:  # No wrapping
            if x1 < x0:
                moves[i].append('u' * x_distance)
            else:
                moves[i].append('d' * x_distance)
        else:  # Wrapping
            if x1 < x0:
                moves[i].append('d' * x_distance + 'w')
            else:
                moves[i].append('u' * x_distance + 'w')

    moves[i].append('p')
    print(moves)
    return x1, y1


def search(key,keyboard,i):#位置

    for char, row in enumerate(keyboard):
        if key in row:
            stringx[i].append(char)
            stringy[i].append(row.index(key))


def verify(string, keyboards):
    kbnum = []
    for keyboard in keyboards:
        if all(any(char in row for row in keyboard) for char in string):
            kbnum.append(keyboards.index(keyboard))
    return kbnum if kbnum else False

def shortest(moves):
    moves0 = [[],[],[],[]]
    for row in range(len(moves)):
        moves0[row] = ''.join(moves[row])

    shortest = max(moves0, key=len)
    index = moves0.index(shortest)
    for i in range(len(moves0)):
        if len(moves0[i]) < len(shortest) and len(moves0[i]) != 0:
            shortest = moves0[i]
            index = i
    return shortest, index
#主函数
string = input("Enter a string to type: ")

num = verify(string,kb)
if num == 0:
    print("The string cannot be typed out.")
    exit(0)

moves = [[], [], [], []] #
stringx = [[], [], [], []]
stringy = [[], [], [], []]

for i in range(len(num)):
    for char in string:
        search(char,kb[num[i]],num[i])

x,y = 0,0
k = 0
for k in range(len(num)):
    for s in range(len(stringx[num[k]])):
        x,y = move(x,y,stringx[num[k]][s],stringy[num[k]][s],num[k])
    x,y = 0,0

shortest0, index_short = shortest(moves)
#print(moves)
#print(shortest0,index_short)
#print(num, stringx, stringy, moves, sep="\n")


print("Configuration used:")
print('-'*(len(kb[index_short][0])+4))
for row in kb[index_short]:
    print(f"| {row} |")
print('-'*(len(kb[index_short][0])+4))

print(f"The robot must perform the following operations:\n{''.join(shortest0)}", sep="\n")
#print(num, stringx, stringy, moves, sep="\n")
