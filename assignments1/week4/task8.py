keyboard_configs = [ ["abcdefghijklm", "nopqrstuvwxyz"],
     ["789", "456", "123",  "0.-"],
    ["chunk", "vibex",  "gymps", "fjord", "waltz"],
    ["bemix", "vozhd","grypt","clunk", "waqfs"]]

def verify(string, keyboards):
    keyboard_verified_num = []
    for keyboard in keyboards:
        if all(any(char in row for row in keyboard) for char in string):
            keyboard_verified_num.append(keyboards.index(keyboard))
    return keyboard_verified_num if keyboard_verified_num else False

def search(key,keyboard,keyboard_config_num):#位置
    for char, row in enumerate(keyboard):
        if key in row:
            char_pos_row[keyboard_config_num].append(char)
            char_pos_col[keyboard_config_num].append(row.index(key))

def move(origin_row, origin_col, target_row, target_col,keyboard_num_config):
    row_distance = target_row - origin_row
    col_distance = target_col - origin_col

    if col_distance < 0:
        moves[keyboard_num_config].append('l'*(-col_distance))
    elif col_distance > 0:
        moves[keyboard_num_config].append('r'*col_distance)
    if row_distance < 0:
        moves[keyboard_num_config].append('u'*(-row_distance))
    elif row_distance > 0:
        moves[keyboard_num_config].append('d'*row_distance)

    moves[keyboard_num_config].append('p')
    return target_row, target_col



def shortest(moves_list):
    filtered_list = [[char for char in row if char != 'w'] for row in moves_list]

    for row in range(len(filtered_list)):
        filtered_list[row] = ''.join(filtered_list[row])

    shortest = min([x for x in filtered_list if len(x) > 0], key=len)
    index = filtered_list.index(shortest)
    return shortest, index
#主函数
string = input("Enter a string to type: ")

keyboard_verified = [[] for num in range(len(keyboard_configs))]
char_pos_row = [[] for num in range(len(keyboard_configs))]
char_pos_col = [[] for num in range(len(keyboard_configs))]
moves = [[] for num in range(len(keyboard_configs))]

keyboard_verified = verify(string,keyboard_configs)
if keyboard_verified == 0:
    print("The string cannot be typed out.")
    exit(0)

for i in range(len(keyboard_verified)):
    for char in string:
        search(char,keyboard_configs[keyboard_verified[i]],keyboard_verified[i])

row,col = 0,0
num = 0
for num in range(len(keyboard_verified)):
    for char in range(len(char_pos_row[keyboard_verified[num]])):
        row,col = move(row,col,char_pos_row[keyboard_verified[num]][char],char_pos_col[keyboard_verified[num]][char], keyboard_verified[num])
    row,col = 0,0
for row in range(len(moves)):
    moves[row] = ''.join(moves[row])


shortest_move, index_short = shortest(moves)
print("Configuration used:")
print('-'*(len(keyboard_configs[index_short][0])+4))
for row in keyboard_configs[index_short]:
    print(f"| {row} |")
print('-'*(len(keyboard_configs[index_short][0])+4))

print(f"The robot must perform the following operations:\n{''.join(moves[index_short])}", sep="\n")
#print(num, stringx, stringy, moves, sep="\n")