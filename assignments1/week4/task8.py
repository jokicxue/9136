'''
The program prompts the user to input a string and calculates which keyboard layouts can type the given string.
It then computes the required movement for typing the string on these available keyboards.
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

def move(origin_row, origin_col, target_row, target_col,keyboard_num_config):
    '''Given the original position, target position, and keyboard config, determine the movement path for Robbie'''
    row_distance = target_row - origin_row
    col_distance = target_col - origin_col

    # choose the column movement direction
    if col_distance < 0:
        moves[keyboard_num_config].append('l'*(-col_distance))
    elif col_distance > 0:
        moves[keyboard_num_config].append('r'*col_distance)

    # choose the row movement direction
    if row_distance < 0:
        moves[keyboard_num_config].append('u'*(-row_distance))
    elif row_distance > 0:
        moves[keyboard_num_config].append('d'*row_distance)

    moves[keyboard_num_config].append('p')
    return target_row, target_col



def shortest(moves_list):
    '''find the shortest movement path between different keyboard configs'''

    #find the shortest movement path excluding empty lists
    shortest = min([x for x in moves_list if len(x) > 0], key=len)

    #find the keyboard configuration for the shortest path
    index = moves_list.index(shortest)
    return shortest, index


#main function
string = input("Enter a string to type: ")

#create lists to store available keyboards, character positions, and movement paths
keyboard_verified = [[] for num in range(len(keyboard_configs))]
char_pos_row = [[] for num in range(len(keyboard_configs))]
char_pos_col = [[] for num in range(len(keyboard_configs))]
moves = [[] for num in range(len(keyboard_configs))]

#verified available keyboards and exit if none are available
keyboard_verified = verify(string,keyboard_configs)
if keyboard_verified == 0:
    print("The string cannot be typed out.")
    exit(0)

#find each key position in all available keyboards and store them in the list
for i in range(len(keyboard_verified)):
    for char in string:
        search(char,keyboard_configs[keyboard_verified[i]],keyboard_verified[i])

#calculate the movement path for Robbie in each available keyboard
row,col = 0,0
num = 0
for num in range(len(keyboard_verified)):
    for char in range(len(char_pos_row[keyboard_verified[num]])):
        row,col = move(row,col,char_pos_row[keyboard_verified[num]][char],char_pos_col[keyboard_verified[num]][char], keyboard_verified[num])
    row,col = 0,0

#flatten the movement list from 2D to 1D to make it easier to process
for row in range(len(moves)):
    moves[row] = ''.join(moves[row])

#find the shortest path and identify it belongs to which keyboard
shortest_move, index_short = shortest(moves)

#print output
print("Configuration used:")
print('-'*(len(keyboard_configs[index_short][0])+4))
for row in keyboard_configs[index_short]:
    print(f"| {row} |")
print('-'*(len(keyboard_configs[index_short][0])+4))
print(f"The robot must perform the following operations:\n{''.join(moves[index_short])}", sep="\n")
