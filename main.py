import time
bool_choice = True
str_userChoice =''

print(" Welcome to my lord of the rings quiz! ")

time.sleep(1.5)
print(" type either a, b, c, d, to awnser a question ") 

time.sleep(2.5)
print(" \n Question 1! ")
time.sleep(0.5)
print(" what is the first lord of the rings movie? ")

time.sleep(2.0)
print(" \n a) The Lord of the Rings: The Fellowship of the Ring ")

time.sleep(0.5)
print(" \n b) The Lord of the Rings: The Return of the King ")

time.sleep(0.5)
print(" \n c) The Lord of the Rings: The Two Towers")

time.sleep(0.5)
print(" \n d) The Lord of the Rings: The Great War of the Ring ")

time.sleep(1.0)
while bool_choice is True:

    str_userChoice == input(" \n what leter will you pick a,b,c,d,\n ")

    if str_userChoice == 'a':  
        print(' Correct ') 
        bool_choice = False 
    
    elif str_userChoice == 'b':
        print(' Incorrect ') 
        bool_choice = False 
    
    elif str_userChoice == 'c':
        print(' Incorrect ') 
        bool_choice = False 
    
    elif str_userChoice == 'd':
        print(' Incorrect ') 
        bool_choice = False 
    
    else:
        print(' Invalid ')
