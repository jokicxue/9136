alist = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
plist = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]
def search_fun(a):
    i = len(alist)
    m = 0
    n = 0
    test = str(input("Enter username:"))
    test1 = str(input(" Enter password:"))
    for m in range(i):
        if test == alist[m]:
            for n in range(i):
                if test1 == plist[n]:
                    print(f" Login successful. Welcome {alist[m]} !")
                    exit(0)
                else:
                    n += 1
        else:
            m += 1
    print(f" Login incorrect. Tries left: {a}")
    return 0


x = 3
while x > 0:
    x -= 1
    search_fun(x)
