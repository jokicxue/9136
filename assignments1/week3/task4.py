"""
This program asks the user to enter a username.
A successful login occurs when the user enters one of the valid usernames.
The program keeps prompting the user until a valid username is provided.
"""

account = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

def search():
    """prompt the user to enter the account, and then verify it"""
    input_account = str(input("Enter username:"))

    ##verify the user's input
    for account_index in range(len(account)):
        if input_account == account[account_index]:
            print(f" Login successful. Welcome {account[account_index]} !")
            exit(0)
        else:
            account_index += 1
    print(" Login incorrect.")
    return 0

#keep prompting
while True:
    search()