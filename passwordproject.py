from doctest import master
import string
import random
# this is to create the master password to make sure you secure all passwords
def view( masterPassword ):
    # this is to ask the question to make the master password
    userPasswordEntered = input( "Please type in your correct master Password: " )
    # this makes an empty list for the passwords to sit in
    allPasswords = []
    # this opens the text file and allows the user to read it
    passwordsFile = open( "passwords.txt", "r" )
    # puts the passwords on a line for user experience to read
    line = passwordsFile.readline()
    
    
    while line != "":
        
        allPasswords.append( line )
        line = passwordsFile.readline()
    # this explains if its not the correct master password it will decline and have a message
    if userPasswordEntered != masterPassword:
        print( "Stop trying to steal from other people's passwords" )
        # if this master password is correct it will allow the user to see the existing passowrds that we are trying to protect 
    else:
        for eachLine in allPasswords:
            print( eachLine )
    
        print( "These are all of your passwords. Stay safe!" )
# this is where the user cna input their information for websites they need to save their password for
def add():
    name = input ('Email: ')
    pwd = input ("Password: ")
    
    
    # this grabs everything and create a text file that shows all your existing/future passwords
    with open('passwords.txt', 'a') as f:
        f.write("Your password on " + str(name) + " is " + str(pwd) + "\n")
        
# this is the main function that makes everything come together
def main():
    masterPassword = input("what is the master password?  ")
    # gives the option to add the password and email for the program the user to use
    while True:
        mode = input("Would you like to add to a new password or view existing ones (view, add), press q to quit? ").lower()
        # if the user uses q it will quit and start over (break)
        if mode == "q":
            break
        if mode == "view":
            view( masterPassword )
        elif mode == "add":
            add()
        else:
            print("invalid mode.")
            continue

main()