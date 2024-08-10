keyboard = ["abcdefghijklm",
            "nopqrstuvwxyz"]

def move(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0

    if y < 0:
        moves.append('l'*(-y))
    elif y > 0:
        moves.append('r'*y)
    if x < 0:
        moves.append('u'*(-x))
    elif x > 0:
        moves.append('d'*x)

    moves.append('p')
    return x1, y1

def search(key):#位置
    for char, row in enumerate(keyboard):
        if key in row:
            stringx.append(char)
            stringy.append(row.index(key))
#主函数
string = input("Enter a string to type: ")
moves = []
if not string.isalpha():
    print(f"The string cannot be typed out.")
    exit(0)

stringx = []
stringy = []

for char in string:
    search(char)

x,y = 0,0

for s in range(len(stringx)):
    x,y = move(x,y,stringx[s],stringy[s])


print(f"The robot must perform the following operations:\n{''.join(moves)}", end = "")

