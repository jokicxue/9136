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

def move(x0, y0, x1, y1,i):
    x = x1 - x0
    y = y1 - y0

    if y < 0:
        moves[i].append('l'*(-y))
    elif y > 0:
        moves[i].append('r'*y)
    if x < 0:
        moves[i].append('u'*(-x))
    elif x > 0:
        moves[i].append('d'*x)

    moves[i].append('p')
    return x1, y1

def search(key,keyboard,i):#位置
    for char, row in enumerate(keyboard):
        if key in row:
            stringx[i].append(char)
            stringy[i].append(row.index(key))


def verify(string,keyboards):
    kbnum = []
    for keyboard in keyboards:
        if all(any(char in row for row in keyboard)for char in string):
            #assert isinstance(keyboard, object)
            kbnum.append(keyboards.index(keyboard))
        #elif keyboards.index(keyboard) == 3 and len(kbnum) > 0:
    return kbnum if kbnum else False

    #return 0
#主函数
string = input("Enter a string to type: ")

num = verify(string,kb)
if num == 0:
    print("Invalid input")
    exit(0)

moves = [[]]
stringx = [[]]
stringy = [[]]


for char in string:
    for i in range(len(num)):
        search(char,kb[num[i]],i)

x,y = 0,0
k = 0
for k in range(len(num)):
    for s in range(len(stringx[k])):
        x,y = move(x,y,stringx[k][s],stringy[k][s],num[k])
    x,y = 0,0

shortest = min(moves,key=len)



print(f"The robot must perform the following operations:\n{''.join(shortest)}", end = "")
