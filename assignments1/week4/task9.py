from assignments1.week4.task7 import keyboard

keyboard_configs = [ ["abcdefghijklm", "nopqrstuvwxyz"],
     ["789", "456", "123",  "0.-"],
    ["chunk", "vibex",  "gymps", "fjord", "waltz"],
    ["bemix", "vozhd","grypt","clunk", "waqfs"]]

def move_distance(origin_pos, target_pos, length):
    direct = abs(origin_pos - target_pos)
    warp = length - direct
    return min(warp, direct),warp

def move(x0, y0, x1, y1, i):
    keyboard = keyboard_configs[i]
    len_row = len(keyboard)
    len_col = len(keyboard[0])

    y_distance, y_sround = move_distance(y0, y1, len_col)
    x_distance, x_sround = move_distance(x0, x1, len_row)

    if y0 != y1:
        if y_distance == abs(y1 - y0) and y_distance != y_sround:  # No wrapping
            if y1 < y0:
                moves[i].append('l' * y_distance)
            else:
                moves[i].append('r' * y_distance)
        else:  # Wrapping
            if y1 < y0:
                for dis in range(y_sround):
                    moves[i].append('r')
                    y0 += 1
                    if y0 == len_col:
                        y0 = 0
                        moves[i].append('w')

            else:
                for dis in range(y_sround):
                    moves[i].append('l')
                    y0 -= 1
                    if y0 == -1:
                        y0 = len_col-1
                        moves[i].append('w')

    if x0 != x1:
        if x_distance == abs(x1 - x0) and x_distance != x_sround:  # No wrapping
            if x1 < x0:
                moves[i].append('u' * x_distance)
            else:
                moves[i].append('d' * x_distance)
        else:  # Wrapping
            if x1 < x0:
                for dis in range(x_sround):
                    moves[i].append('d')
                    x0 += 1
                    if x0 == len_row:
                        x0 = 0
                        moves[i].append('w')
            else:
                for dis in range(x_sround):
                    moves[i].append('u')
                    x0 -= 1
                    if x0 == -1:
                        x0 = len_row-1
                        moves[i].append('w')
    moves[i].append('p')
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
    filtered_list = [[],[],[],[]]
    moves1 = [[],[],[],[]]
    for row in range(len(moves)):
        moves0[row] = ''.join(moves[row])

    for x in range(len(moves0)):
        filtered = list(filter(lambda x: x != 'w', moves0[x]))
        moves1[x] = filtered

    for row in range(len(moves1)):
        filtered_list[row] = ''.join(moves1[row])

    shortest = max(filtered_list, key=len)
    index = filtered_list.index(shortest)
    for i in range(len(filtered_list)):
        if len(filtered_list[i]) < len(shortest) and len(filtered_list[i]) != 0:
            shortest = filtered_list[i]
            index = i
    return shortest, index,moves0[index]


#主函数
string = input("Enter a string to type: ")

keyboard_verified = verify(string,keyboard_configs)
if keyboard_verified == 0:
    print("The string cannot be typed out.")
    exit(0)

moves = [[], [], [], []] #
stringx = [[], [], [], []]
stringy = [[], [], [], []]

for i in range(len(keyboard_verified)):
    for char in string:
        search(char,keyboard_configs[keyboard_verified[i]],keyboard_verified[i])

x,y = 0,0
k = 0
for k in range(len(keyboard_verified)):
    for s in range(len(stringx[keyboard_verified[k]])):
        x,y = move(x,y,stringx[keyboard_verified[k]][s],stringy[keyboard_verified[k]][s],keyboard_verified[k])
    x,y = 0,0

shortest0, index_short, movelist = shortest(moves)

print("Configuration used:")
print('-'*(len(keyboard_configs[index_short][0])+4))
for row in keyboard_configs[index_short]:
    print(f"| {row} |")
print('-'*(len(keyboard_configs[index_short][0])+4))

print(f"The robot must perform the following operations:\n{''.join(movelist)}", sep="\n")
