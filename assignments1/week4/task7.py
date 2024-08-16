keyboard = ["abcdefghijklm",
            "nopqrstuvwxyz"]

def move(origin_row, origin_col, target_row, target_col):
    row_distance = target_row - origin_row
    col_distance = target_col - origin_col

    if col_distance < 0:
        moves.append('l'*(-col_distance))
    elif col_distance > 0:
        moves.append('r'*col_distance)
    if row_distance < 0:
        moves.append('u'*(-row_distance))
    elif row_distance > 0:
        moves.append('d'*row_distance)

    moves.append('p')
    return target_row, target_col

def search(key):#位置
    for char, row in enumerate(keyboard):
        if key in row:
            char_pos_row.append(char)
            char_pos_col.append(row.index(key))
#主函数
string = input("Enter a string to type: ")
moves = []
if not string.isalpha():
    print(f"The string cannot be typed out.")
    exit(0)

char_pos_row = []
char_pos_col = []

for char in string:
    search(char)

row,col = 0,0

for s in range(len(char_pos_row)):
    row,col = move(row,col,char_pos_row[s],char_pos_col[s])


print(f"The robot must perform the following operations:\n{''.join(moves)}", end = "")

