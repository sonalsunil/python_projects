#password generator
import random, pyperclip
import string

while True:
    try:
        l = int(input("Enter the length of the password: "))

        if l > 0:
            break
        else:
            print("Enter a positive number.")

    except ValueError:
        print("Enter a valid number.")

uc=input("uppercase:yes/no?")
lc=input("lowercase:yes/no?")
nos=input("numbers:yes/no?" )
symb=input("symbols:yes/no?")

symbols="$#@&"

#create character pool 
pas=""
if uc=="yes":
    pas=pas+string.ascii_uppercase
if lc=="yes":
    pas=pas+string.ascii_lowercase
if nos=="yes":
    pas=pas+string.digits
if symb=="yes":
    pas=pas+symbols


# count the selected character types
password = ""
count = 0

if uc == "yes":
    count += 1

if lc == "yes":
    count += 1

if nos == "yes":
    count += 1

if symb == "yes":
    count += 1

   
if pas == "":
    print("Please select at least one character type.") 

elif l<count:
    print("Password length is too small .")

else:
    if uc =="yes":
        password=password +random.choice(string.ascii_uppercase)

    if lc =="yes":
        password=password +random.choice(string.ascii_lowercase)
    
    if nos=="yes":
        password=password +random.choice(string.digits)
   
    if symb=="yes":
        password=password +random.choice(symbols)

    while (len(password)<l):
        password= password+random.choice(pas)
    print(password)

#copy password to clipboard
if(password):
    pyperclip.copy(password)
    print("Password copied to clipboard.")
    
    
