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

while bool_choice is True:

    time.sleep(1.0)
    str_userChoice = input(" \n what leter will you pick a,b,c,d,\n ")

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

pass

time.sleep(0.5)
print(" \n Question 2! ")
time.sleep(0.5)
print(" In the first lord of the rings movie who is the main character? ")

time.sleep(2.0)
print(" \n a) Gollum ")

time.sleep(0.5)
print(" \n b) Legolas ")

time.sleep(0.5)
print(" \n c) Frodo ")

time.sleep(0.5)
print(" \n d) Gandalf ")

while bool_choice is False:

    time.sleep(1.0)
    str_userChoice = input(" \n what leter will you pick a,b,c,d,\n ")

    if str_userChoice == 'a':  
        print(' Incorrect ') 
        bool_choice = True 
    
    elif str_userChoice == 'b':
        print(' Incorrect ') 
        bool_choice = True 
    
    elif str_userChoice == 'c':
        print(' Correct ') 
        bool_choice = True 
    
    elif str_userChoice == 'd':
        print(' Incorrect ') 
        bool_choice = True 
    
    else:
        print(' Invalid ')
        
pass

time.sleep(0.5)
print(" \n Question 3! ")
time.sleep(0.5)
print(" What is gandalfs iconic line? ")

time.sleep(2.0)
print(" \n a) You shall fall beneath my blade! ")

time.sleep(0.5)
print(" \n b) Fall before my might! ")

time.sleep(0.5)
print(" \n c) You will not take one more step! ")

time.sleep(0.5)
print(" \n d) You shall not pass! ")

while bool_choice is True:

    time.sleep(1.0)
    str_userChoice = input(" \n what leter will you pick a,b,c,d,\n ")

    if str_userChoice == 'a':  
        print(' Incorrect ') 
        bool_choice = False 
    
    elif str_userChoice == 'b':
        print(' Incorrect ') 
        bool_choice = False 
    
    elif str_userChoice == 'c':
        print(' Incorrect ') 
        bool_choice = False 
    
    elif str_userChoice == 'd':
        print(' Correct ') 
        bool_choice = False 
    
    else:
        print(' Invalid ')
        
pass

time.sleep(0.5)
print(" \n Question 4! ")
time.sleep(0.5)
print(" What is gollums iconic line? ")

time.sleep(2.0)
print(" \n a) my pretty ")

time.sleep(0.5)
print(" \n b) Get away! ")

time.sleep(0.5)
print(" \n c) My precious ")

time.sleep(0.5)
print(" \n d) MINE! ")

while bool_choice is False:

    time.sleep(1.0)
    str_userChoice = input(" \n what leter will you pick a,b,c,d,\n ")

    if str_userChoice == 'a':  
        print(' Incorrect ') 
        bool_choice = True 
    
    elif str_userChoice == 'b':
        print(' Incorrect ') 
        bool_choice = True 
    
    elif str_userChoice == 'c':
        print(' Correct ') 
        bool_choice = True 
    
    elif str_userChoice == 'd':
        print(' Incorrect ') 
        bool_choice = True 
    
    else:
        print(' Invalid ')
