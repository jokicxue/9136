'''
The program prompt the user to input a string and calculate which keyboard layouts can type the given string.
It then computes the required movement for typing the string on these available keyboards, considering
that the robot Robbie can wrap around the keyboard.
Finally, it identifies the keyboard configuration that results in the shortest movement path
and outputs both the chosen keyboard and the required displacement.
'''
keyboard_configs = [ ["abcdefghijklm", "nopqrstuvwxyz"],
     ["789", "456", "123",  "0.-"],
    ["chunk", "vibex",  "gymps", "fjord", "waltz"],
    ["bemix", "vozhd","grypt","clunk", "waqfs"]]

def verify(string, keyboards):
    '''check which keyboard config can be typed'''
    keyboard_verified_num = []
    for keyboard in keyboards:
        if all(any(char in row for row in keyboard) for char in string):
            keyboard_verified_num.append(keyboards.index(keyboard))
    return keyboard_verified_num if keyboard_verified_num else False

def search(key,keyboard,keyboard_config_num):
    '''search the key position on the specific keyboard and add it to the list'''
    for char, row in enumerate(keyboard):
        if key in row:
            char_pos_row[keyboard_config_num].append(char)
            char_pos_col[keyboard_config_num].append(row.index(key))

def move_distance(origin_pos, target_pos, length):
    '''Calculate the distance between two positions using different movement patterns and compare the results'''
    direct = abs(origin_pos - target_pos)
    warp = length - direct
    return min(warp, direct),warp

def move(origin_row, origin_col, target_row, target_col, keyboard_num_config):
    '''Given the original position, target position, and keyboard config, determine the movement path for Robbie'''
    keyboard = keyboard_configs[keyboard_num_config]
    len_row = len(keyboard)
    len_col = len(keyboard[0])

    col_distance, col_warp_distance = move_distance(origin_col, target_col, len_col)
    row_distance, row_warp_distance = move_distance(origin_row, target_row, len_row)
    #choose the column movement pattern
    if origin_col != target_col:
        # No wrapping
        if col_distance == abs(target_col - origin_col) and col_distance != col_warp_distance:
            if target_col < origin_col:
                moves[keyboard_num_config].append('l' * col_distance)
            else:
                moves[keyboard_num_config].append('r' * col_distance)
        # Wrapping
        else:
            if target_col < origin_col:
                #add the movement path per step
                for dis in range(col_warp_distance):
                    moves[keyboard_num_config].append('r')
                    origin_col += 1
                    #add 'w' when reaching the edge and wrapping the index
                    if origin_col == len_col:
                        origin_col = 0
                        moves[keyboard_num_config].append('w')

            else:
                for dis in range(col_warp_distance):
                    moves[keyboard_num_config].append('l')
                    origin_col -= 1
                    if origin_col == -1:
                        origin_col = len_col-1
                        moves[keyboard_num_config].append('w')
    # choose the row movement pattern
    if origin_row != target_row:
        # No wrapping
        if row_distance == abs(target_row - origin_row) and row_distance != row_warp_distance:
            if target_row < origin_row:
                moves[keyboard_num_config].append('u' * row_distance)
            else:
                moves[keyboard_num_config].append('d' * row_distance)
        # Wrapping
        else:
            if target_row < origin_row:
                # add the movement path per step
                for dis in range(row_warp_distance):
                    moves[keyboard_num_config].append('d')
                    origin_row += 1
                    # add 'w' when reaching the edge and wrapping the index
                    if origin_row == len_row:
                        origin_row = 0
                        moves[keyboard_num_config].append('w')
            else:
                for dis in range(row_warp_distance):
                    moves[keyboard_num_config].append('u')
                    origin_row -= 1
                    if origin_row == -1:
                        origin_row = len_row-1
                        moves[keyboard_num_config].append('w')
    moves[keyboard_num_config].append('p')
    return target_row, target_col

def shortest(moves_list):
    '''find the shortest movement path between different keyboard configs'''
    #remove the 'w' because it does not count for a step
    filtered_list = [[char for char in row if char != 'w'] for row in moves_list]
    #flatten the list from 2D to 1D
    for row in range(len(filtered_list)):
        filtered_list[row] = ''.join(filtered_list[row])
    #find the shortest movement path excluding empty lists
    shortest = min([x for x in filtered_list if len(x) > 0], key=len)
    #find the keyboard configuration for the shortest path
    index = filtered_list.index(shortest)
    return shortest, index

#main function
input_string = input("Enter a string to type: ")
#create lists to store available keyboards, character positions, and movement paths
keyboard_verified = [[] for num in range(len(keyboard_configs))]
char_pos_row = [[] for num in range(len(keyboard_configs))]
char_pos_col = [[] for num in range(len(keyboard_configs))]
moves = [[] for num in range(len(keyboard_configs))]
#verified available keyboards and exit if none are available
keyboard_verified = verify(input_string,keyboard_configs)
if keyboard_verified == 0:
    print("The string cannot be typed out.")
    exit(0)
#find each key position in all available keyboards and store them in the list
for i in range(len(keyboard_verified)):
    for char in input_string:
        search(char,keyboard_configs[keyboard_verified[i]],keyboard_verified[i])
#calculate the movement path for Robbie in each available keyboard
row,col = 0,0
num = 0
for num in range(len(keyboard_verified)):
    for char in range(len(char_pos_row[keyboard_verified[num]])):
        row,col = move(row,col,char_pos_row[keyboard_verified[num]][char],char_pos_col[keyboard_verified[num]][char],keyboard_verified[num])
    row,col = 0,0
#flatten the movement list from 2D to 1D to make it easier to process
for row in range(len(moves)):
    moves[row] = ''.join(moves[row])
#find the shortest path and identify it belongs to which keyboard
shortest_move, index_short = shortest(moves)
print("Configuration used:")
print('-'*(len(keyboard_configs[index_short][0])+4))
for row in keyboard_configs[index_short]:
    print(f"| {row} |")
print('-'*(len(keyboard_configs[index_short][0])+4))
print(f"The robot must perform the following operations:\n{moves[index_short]}", sep="\n")

