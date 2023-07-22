# Libraries we will use
import string
import random


# Define functions to be used
def write():
    account_platform = input(
        "Enter the platform(website/app) of the account: ")
    account_name = input(
        "Enter username/email: ")
    with open("passwords.txt", "a") as store_file:
        store_file.write(
            f"===============================\n\t\t{account_platform.upper()}\n===============================\nusername: {account_name}\npassword: {password}\n===============================\n\n")


# Lists to store characters, numbers and alphabetical
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number = input("How many characters for the password? ")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print("PLEASE USE 6 OR MORE CHARCTERS")
            characters_number = input("Please enter the number again: ")
        else:
            break
    except:
        print("Please enter numbers only")
        characters_number = input("How many characters for the password? ")

# Shuffle lists to get random arrange
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Get 30% from alphabetical and 20% from digits
# We will generate a password with 60% alphabeticals and 40% digits characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

password = []

# Loop to generate 60% of the length (upper and lower cases)
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

# Loop to generate 40% of the length (Digits and characters)
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

# Shuffle the generated password again
random.shuffle(password)

# Convert the generated password from list to string
password = "".join(password[0:])

# Say welcome to the generated password
choice = input(
    "Enter a choice: (1) Display password here\t(2) Store the password at text file\n:")
while True:
    try:
        choice = int(choice)
        if choice != 1 and choice != 2:
            choice = input(
                "Enter a valid choice: ")
        else:
            break
    except:
        print("ENTER A VALID CHOICE: ")
        choice = input(
            "Enter a choice: (1) Display password here\t(2) Store the password at text file\n:")

if choice == 1:
    print(password)
else:
    write()
