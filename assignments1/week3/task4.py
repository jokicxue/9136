account = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

def search():
    input_account = str(input("Enter username:"))
    for account_index in range(len(account)):
        if input_account == account[account_index]:
            print(f" Login successful. Welcome {account[account_index]} !")
            exit(0)
        else:
            account_index += 1
    print(" Login incorrect.")
    return 0


while True:
    search()