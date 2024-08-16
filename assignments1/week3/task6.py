'''
This program prompts the user to enter a valid username and password.
The program allows up to 3 attempts to enter the correct login.
If the user fails after 3 attempts, they are asked if they are a robot.
If they are not a robot, they receive 3 additional tries.
If they are a robot, the program terminates.
'''

account = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
password = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]

def search(try_times):
    '''prompt the user to enter the account and password, and then verify them'''
    input_account = str(input("Enter username:"))
    input_passwd = str(input(" Enter password:"))

    #verify the user's input
    for user_index in range(len(account)):
        if input_account == account[user_index]:
            if input_passwd == password[user_index]:
                print(f" Login successful. Welcome {account[user_index]} !")
                exit(0)
            else:
                break
        else:
            user_index += 1
    print(f" Login incorrect. Tries left: {try_times}")
    return 0

#specify the number of tries
log_try = 3
while log_try > 0:
    log_try -= 1
    search(log_try)
    #human-computer testing
    while log_try == 0:
        robo_test = str(input("Are you a robot (Y/n)? "))
        if robo_test == "n":
            log_try = 3
            break
        elif robo_test == "Y":
            exit(0)
        elif robo_test == "":
            exit(0)
        else:
            continue