keyboard = ["abcdefghijklm",
            "nopqrstuvwxyz"]

def move(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0

    if x < 0:
        moves.append('l'*(-x))
    elif x > 0:
        moves.append('r'*x)
    if y < 0:
        moves.append('u'*(-y))
    elif y > 0:
        moves.append('d'*y)

    moves.append('p')
    return x1,y1

#主函数
string = input("Enter a string to type:")
moves = []
if not string.isalpha():
    print(f"The string cannot be typed out.")
    exit(0)
a=0
stringx= []
stringy = []
#位置
def search(key):
    for char, row in enumerate(keyboard):
        if key in row:
            stringx.append(char)
            stringy.append(row.index(key))





x,y = 0,0
print(f"The robot must perform the following operations:", end = "")

for s in range(len(string)):
    move(x,y,stringx[s],stringy[s])



