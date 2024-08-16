kb = [ ["abcdefghijklm", "nopqrstuvwxyz"], ["789", "456", "123", "0.-"],
       ["chunk", "vibex", "gymps", "fjord","waltz"], ["bemix","vozhd", "grypt", "clunk", "waqfs"]]

def move_distance(origin_pos, target_pos, length):
    direct = abs(origin_pos - target_pos)
    warp = length - direct
    return min(warp, direct),warp

def move(x0, y0, x1, y1, i):
    keyboard = kb[i]
    num_row = len(keyboard)
    num_col = len(keyboard[0])

    y_distance, y_sround = move_distance(y0, y1, num_col)
    x_distance, x_sround = move_distance(x0, x1, num_row)

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
                for dis in range(y_sround):
                    moves[i].append('r')
                    y0 += 1
                    if y0 == num_col:
                        y0 = 0
                        moves[i].append('w')

                    #moves[i].append('r' * y_distance + 'w')
            else:
                for dis in range(y_sround):
                    moves[i].append('l')
                    y0 -= 1
                    if y0 == -1:
                        y0 = num_col-1
                        moves[i].append('w')


                #moves[i].append('l' * y_distance + 'w')

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
                    if x0 == num_row:
                        x0 = 0
                        moves[i].append('w')
                #moves[i].append('d' * x_distance + 'w')
            else:
                for dis in range(x_sround):
                    moves[i].append('u')
                    x0 -= 1
                    if x0 == -1:
                        x0 = num_row-1
                        moves[i].append('w')
                #moves[i].append('u' * x_distance + 'w')

    moves[i].append('p')
    #print(moves)
    return x1, y1


def search(key,keyboard,keyboard_config_num):#位置

    for char, row in enumerate(keyboard):
        if key in row:
            stringx[keyboard_config_num].append(char)
            stringy[keyboard_config_num].append(row.index(key))


def verify(string, keyboards):
    keyboard_num = []
    for keyboard in keyboards:
        if all(any(char in row for row in keyboard) for char in string):
            keyboard_num.append(keyboards.index(keyboard))
    return keyboard_num if keyboard_num else False


def shortest(moves_list):
    filtered_list = [[char for char in row if char != 'w'] for row in moves_list]

    for row in range(len(filtered_list)):
        filtered_list[row] = ''.join(filtered_list[row])

    # shortest = min([x for x in filtered_list if x != 0])
    # index = filtered_list.index(shortest)
    shortest = max(filtered_list, key=len)
    index = filtered_list.index(shortest)
    for i in range(len(filtered_list)):
        if len(filtered_list[i]) < len(shortest) and len(filtered_list[i]) != 0:
            shortest = filtered_list[i]
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
for row in range(len(moves)):
    moves[row] = ''.join(moves[row])
shortest0, index_short= shortest(moves)
#print(moves)
#print(shortest0,index_short)
#print(num, stringx, stringy, moves, sep="\n")


print("Configuration used:")
print('-'*(len(kb[index_short][0])+4))
for row in kb[index_short]:
    print(f"| {row} |")
print('-'*(len(kb[index_short][0])+4))

print(f"The robot must perform the following operations:\n{''.join(moves[index_short])}", sep="\n")
#print(num, stringx, stringy, sep="\n")
#print(f"{''.join(moves[0])},{''.join(moves[1])},{''.join(moves[2])},{''.join(moves[3])}")