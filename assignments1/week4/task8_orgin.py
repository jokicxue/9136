keyboard_configs = [ ["abcdefghijklm", "nopqrstuvwxyz"],
     ["789", "456", "123",  "0.-"],
    ["chunk", "vibex",  "gymps", "fjord", "waltz"],
    ["bemix", "vozhd","grypt","clunk", "waqfs"]]

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
    #print(i,moves)
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
    for row in range(len(moves)):
        moves0[row] = ''.join(moves[row])

    shortest = max(moves0, key=len)
    index = moves0.index(shortest)
    for i in range(len(moves0)):
        if len(moves0[i]) < len(shortest) and len(moves0[i]) != 0:
            shortest = moves0[i]
            index = i
    return shortest, index
#主函数
string = input("Enter a string to type: ")

num = verify(string,keyboard_configs)
if num == 0:
    print("The string cannot be typed out.")
    exit(0)

moves = [[], [], [], []] #
stringx = [[], [], [], []]
stringy = [[], [], [], []]

for i in range(len(num)):
    for char in string:
        search(char,keyboard_configs[num[i]],num[i])

x,y = 0,0
k = 0
for k in range(len(num)):
    for s in range(len(stringx[num[k]])):
        x,y = move(x,y,stringx[num[k]][s],stringy[num[k]][s],num[k])
    x,y = 0,0

shortest0, index_short = shortest(moves)
#print(moves)
#print(shortest0,index_short)
#print(num, stringx, stringy, moves, sep="\n")


print("Configuration used:")
print('-'*(len(keyboard_configs[index_short][0])+4))
for row in keyboard_configs[index_short]:
    print(f"| {row} |")
print('-'*(len(keyboard_configs[index_short][0])+4))

print(f"The robot must perform the following operations:\n{''.join(shortest0)}", sep="\n")
#print(num, stringx, stringy, moves, sep="\n")
