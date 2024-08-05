Keyboard = ["abcdefghijklm",
            "nopqrstuvwxyz"]

def move(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0

    if x < 0:
        print('l'*(-x))
    elif x > 0:
        print('r'*x)
    if y < 0:
        print('u'*(-y))
    elif y > 0:
        print('d'*y)

    print('p')
    return x1,y1


string = input("Enter a string to type:")

if not string.isalpha():
    print(f"The string cannot be typed out.")
    exit(0)
a=0
stringx= []
stringy = []
for b in range(len(string)):
    for i in range(2) :
        for j in range(14):
             if string[b] == Keyboard[i][j]:
                 stringx.append(j)
                 stringy.append(i)
                 a += 1
    b = b+1


x,y = 0,0
print(f"The robot must perform the following operations:", end = "")

for s in range(len(string)):
    move(x,y,stringx[s],stringy[s])



