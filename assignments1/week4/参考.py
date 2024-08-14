kb = [
    ["abcdefghijklm", "nopqrstuvwxyz"],
    ["789", "456", "123", "0.-"],
    ["chunk", "vibex", "gymps", "fjord", "waltz"],
    ["bemix", "vozhd", "grypt", "clunk", "waqfs"]
]


def wrap_around_distance(pos1, pos2, length):
    """计算包裹距离"""
    direct_distance = abs(pos1 - pos2)
    wrap_distance = length - direct_distance
    return min(direct_distance, wrap_distance)


def move(x0, y0, x1, y1, i):
    keyboard = kb[i]
    num_rows = len(keyboard)
    num_cols = len(keyboard[0])

    # 计算水平和垂直距离
    y_distance = wrap_around_distance(y0, y1, num_cols)
    x_distance = wrap_around_distance(x0, x1, num_rows)

    if y0 != y1:
        if y1 < y0:
            moves[i].append('l' * y_distance + 'w')
        else:
            moves[i].append('r' * y_distance + 'w')
    if x0 != x1:
        if x1 < x0:
            moves[i].append('u' * x_distance + 'w')
        else:
            moves[i].append('d' * x_distance + 'w')

    moves[i].append('p')
    return x1, y1


def search(key, keyboard, i):
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
    moves0 = [''.join(m) for m in moves]
    shortest = min(moves0, key=len, default='')
    index = moves0.index(shortest) if shortest in moves0 else -1
    return shortest, index


# 主函数
string = input("Enter a string to type: ")
kb_choice = int(input("Choose a keyboard (0 to {}): ".format(len(kb) - 1)))

if kb_choice < 0 or kb_choice >= len(kb):
    print("Invalid keyboard choice.")
    exit(0)

num = verify(string, kb)
if not num:
    print("The string cannot be typed out.")
    exit(0)

moves = [[] for _ in range(len(kb))]
stringx = [[] for _ in range(len(kb))]
stringy = [[] for _ in range(len(kb))]

for i in range(len(num)):
    for char in string:
        search(char, kb[num[i]], num[i])

x, y = 0, 0
for k in num:
    for s in range(len(stringx[k])):
        x, y = move(x, y, stringx[k][s], stringy[k][s], k)
    x, y = 0, 0

shortest0, index_short = shortest(moves)
index_kb = num[index_short] if index_short != -1 else -1

if index_kb != -1:
    print("Configuration used:")
    print('-' * (len(kb[index_kb][0]) + 4))
    for row in kb[index_kb]:
        print(f"| {row} |")
    print('-' * (len(kb[index_kb][0]) + 4))
    print(f"The robot must perform the following operations:\n{''.join(shortest0)}", sep="\n")
else:
    print("No valid keyboard layout found.")
