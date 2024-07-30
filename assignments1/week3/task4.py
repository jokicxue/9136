alist = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

def search_fun():
    #i = len(alist)
    i = len(alist)
    m = 0
    test = str(input("Enter username:"))
    for m in range(i):
        #print(f"{alist[m]}")
        if test == alist[m]:
            print(f"Login successful. Welcome {alist[m]}\n")
            exit(0)
        else:
            m += 1
    print("Login incorrect.")

    return 0


a = 1
while a:
    search_fun()