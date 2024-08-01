'''
This program
'''
account = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
password = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]
def search_fun(t):
    i = len(account)
    m = 0
    n = 0
    input_account = str(input("Enter username:"))
    input_passwd = str(input(" Enter password:"))
    for m in range(i):
        if input_account == account[m]:
            for n in range(i):
                if input_passwd == password[n]:
                    print(f" Login successful. Welcome {account[m]} !")
                    exit(0)
                else:
                    n += 1
        else:
            m += 1
    print(f" Login incorrect. Tries left: {t}")
    return 0


log_try = 3
while log_try > 0:
    log_try -= 1
    search_fun(log_try)
