'''
This program prompts the user to enter a valid username and password.
The program allows up to 3 attempts to enter the correct login.
'''

account = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
password = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]

def search(try_times):
    '''prompt the user to enter the account and password, and then verify them'''
    input_account = str(input("Enter username:"))
    input_passwd = str(input(" Enter password:"))

    # verify the user's input
    for account_index in range(len(account)):
        if input_account == account[account_index]:
            for password_index in range(len(account)):
                if input_passwd == password[password_index]:
                    print(f" Login successful. Welcome {account[account_index]} !")
                    exit(0)
                else:
                    password_index += 1
        else:
            account_index += 1
    print(f" Login incorrect. Tries left: {try_times}")
    return 0

#specify the number of tries
log_try = 3
while log_try > 0:
    log_try -= 1
    search(log_try)
