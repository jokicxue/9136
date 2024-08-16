'''
The program asks the user to input a string,
and plans the actions for Robbie the robot to type this string on a keyboard.
It also outputs the list of movement required for the robot to complete the task
'''

keyboard = ["abcdefghijklm",
            "nopqrstuvwxyz"]

def search(key):
    '''search the key position on the keyboard and add it to the list'''
    for char, row in enumerate(keyboard):
        if key in row:
            char_pos_row.append(char)
            char_pos_col.append(row.index(key))

def move(origin_row, origin_col, target_row, target_col):
    '''Given the original position, target position, and keyboard config, determine the movement path for Robbie'''
    row_distance = target_row - origin_row
    col_distance = target_col - origin_col

    # choose the column movement direction
    if col_distance < 0:
        moves.append('l'*(-col_distance))
    elif col_distance > 0:
        moves.append('r'*col_distance)

    # choose the row movement direction
    if row_distance < 0:
        moves.append('u'*(-row_distance))
    elif row_distance > 0:
        moves.append('d'*row_distance)

    moves.append('p')
    return target_row, target_col


#main function
string = input("Enter a string to type: ")

#create lists to store character positions, and movement paths
char_pos_row = []
char_pos_col = []
moves = []

#check if the keyboard can type the string and exit if it cannot
if not string.isalpha():
    print(f"The string cannot be typed out.")
    exit(0)

#find each key position on keyboard and store them in the list
for char in string:
    search(char)

#calculate the movement path for Robbie on keyboard
row,col = 0,0
for s in range(len(char_pos_row)):
    row,col = move(row,col,char_pos_row[s],char_pos_col[s])

#print output
print(f"The robot must perform the following operations:\n{''.join(moves)}", end = "")

