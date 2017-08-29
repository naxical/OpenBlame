# Program Made To Generate Secure Password Phrases

import random


alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#&*^!%$~"
pw_length = 10 # set this value to how long you want your password to be; do not set to anything over 71 characters
mypw = ""

for i in range(pw_length):
    next_index = random.randrange(len(alphabet))
    mypw = mypw + alphabet[next_index]

passtype = raw_input("What service are you using? ")
print passtype
line = "Your password for " + passtype + " is : " + mypw
print line

writeyn = raw_input("Would you like to write your password to a text file? Y/n")
writeyn = writeyn.strip() # makes sure that no white space is around

if writeyn == 'Y':
    print('Written to passwords.txt')
    f = open("passwords.txt", "a+") # "append"
    f.write(passtype + " - " + mypw)

if writeyn == 'n':
    print('Writting Stopped.')

while writeyn != 'n' and writeyn != 'Y':
    writeyn = raw_input("Invalid Input, Please Enter Y or n; " + "\nWould you like to write your password to a text file? Y/n")
    writeyn = writeyn.strip()
    if writeyn == 'n' or writeyn == 'N' or writeyn == 'no' or writeyn == 'No':
        print 'Writing Stopped.'
        break
    elif writeyn == 'Y' or writeyn == 'y' or writeyn == 'yes' or writeyn == 'Yes':
        print('Written to passwords.txt')
        f = open("passwords.txt", "a+")
        f.write(passtype + " - " + mypw)
        break
