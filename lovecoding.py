# allThingsthrough=input("Christ Jesus")

# python-basics-weekly-3
# Create a bank program.
#
# YOU MUST COMMENT THIS PROJECT AND WRITE OUT A STEP BY STEP PLAN OF WHAT YOU WILL CODE, THEN TEST (PLAN.TXT).
# Reoccuring options (2.5 points)
#
# Give the user the following options. Once the option that is selected is completed keep asking them until they hit 4 to quit:
#
# Hello, please choose one of following options:
# 1) Check balance
# 2) Add money to account
# 3) Withdraw money from account
# 4) Quit
# What will you like to do?
# Check Balance (2.5 points)
#
# Check balance should show the current balance. Make sure a $ sign is in the sentence.
#
# Example: Your account has $200 dollars


#
# Add money to account (2.5 points)
#
# Once this selection is chosen, ask the user how much money they want to deposit. Update their account, then print the updated balance.
#
# Example: How much would you like to deposit?
#
# Example: Your account now holds $205 dollars
#
# Withdraw money from account (2.5 points)
#
# Once this selection is chosen, ask the user how much money they want to withdraw. If they don't have enough money in the account, print "Insufficient funds". Otherwise, update their account, then print the updated balance.
#
# Challenge
#
# Before the program starts, ask the user for their account name and a pin number.
#
# Instead of using "you", use the account user's name
# Before allowing them to withdraw, check to see if they know the pin number.
# If they don't get the correct pin, ask them to try again.
# SERIOUSLY, POINTS WILL BE TAKEN OFF FOR NOT COMMENTING

# // Setup main menu command loop options to give user to choose from

### There are references to fixed dollar amounts like 3000, 2000 and 5000 in your prompt
### when you are getting User input.
### The user can enter any number, not just those amounts. You should use whatever number
### they enter in your balance calculation for a deposit or withdraw.

### You have the beginnings of a menu, but it only prints at start and is not wrapped in a main
### control loop so User continues until they quit.
### You have some of the code needed for the menu options, but you are not using conditionals (if)
### to check what number the user entered and only run the code for selected feature (ex. Deposit)
### before returning to the main menu.

### As submitted, won't run because of partial piece of code at bottom. If you comment that out,
### it runs, and does some of what it needs to do, but the functionality wasn't separated into separate code blocks
### with proper if statements and those if blocks weren't wrapped in a main control loop block so it would let the
### user do more than one action until quit.


bankUser=-2
print(

 '1. checkBalance'
 '2. deposit'
 '3. withdraw'
 '4. quit'

)
# Options that allow the uset to choose with transaction they would like
bankUser = int (input('Enter the number of the menu option you want'))
bankUserbalance = str (input(" The balance of the account is $3000.00"))

# Check and respond to the menu item selected by the user
# if bankUser == 1_( #user selected they want to check their balance

# What is the available balance?

print
(bankUserbalance)



# Check and respond to the menu item selected by the user
# if bankUser == 2_( #user selected they want to deposit money in the

bankUser2 = int (input('Enter the number of the menu option you want'))
bankUser2=int(input("How much money do you want to deposit into the account?"))
bankUserDeposit2 = str (input("I want to deposit $2000.00 in the account"))
bankUser2= str (input("New Balance is $5000.00"))

print( bankUserDeposit2)
print (bankUser2)

# Check and respond to the menu item selected by the user
# if bankUser == 3_( #user selected they want to withdraw money)
bankUser3 = int (input('Enter the number of the menu option you want'))
bankUser3=(input("I want to withdraw $5500.00 from the account"))
nomoney= ("insufficient funds")
if bankUser3 < 5000.00:
    print (nomoney)

### Always submit assignment code will run.
### Push your changes frequently after every completed and tested addition and before
### you go on to the next requirement. Then if you run out of time, you can just stick with
### your most reason version of your program that containing code that worked. And you get
### credit for what code does run. If we can't run the final submission, we can't test the code that was completed.
### NOTE seems you did remove the broken code so good job! Unfortunately that was at 5:04 so I didn't see it. Still, advice above applies for every assignment project.
if bankUser
