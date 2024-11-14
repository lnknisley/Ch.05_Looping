# 5.0 Jedi Training (50pts)  Name:________________

'''
 1. Make the following program work. LIST THE 3 MISTAKES (5pts)
   '''
print("This program takes three integers and returns the sum.")
     total = 0
     for i in range(3):
         x = int(input("Enter a number: "))
         total+=x
     print("The total is:", total)

#1 the input function needs an int wrapper
#2 x is undefined and should be the total variable
#3 i should not be to the added value to the total, x should be as it's the input


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive. (5pts)
'''
for i in range(2, 102, 2):
    print(i)





'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop. (5pts)
'''
x = 10
while x > -1:
    print(x)
    x -= 1
print("Blast off!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive). (5pts)
'''
import random
x = random.randint(1, 11)
print(x)




'''
  5. 7 NUMBER ANALYSIS (5pts)
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
pos = 0
neg = 0
nil = 0
for i in range(7):
    num = int(input("Number please? "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        nil += 1
print("# of positive numbers:", pos, "\n# of negative numbers:", neg, "\n# of zeros:", nil)




'''
6. COIN TOSS PROGRAM (10pts)
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
tails = 0
heads = 0
for i in range(50):
    coin = random.randint(0, 1)
    if coin == 0:
        print("Heads!")
        heads += 1
    else:
        print("Tails!")
        tails += 1
print("# of heads:", heads, "\n# of tails:", tails)




'''
ROSHAMBO PROGRAM (15pts)
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round, tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits, print an end game message and their win/loss/tie record

'''
import random
python_ws = 0
human_ws = 0
draws = 0

def num_to_sign(y):
    if y == 1:
        return "Rock!"
    elif y == 2:
        return "Paper!"
    else:
        return "Scissors!"

while True:
    computer = random.randint(1, 3)
    ask = int(input("Place your pick or leave (1. Rock, 2. Paper, 3. Scissors, 4. Exit) "))
    if ask == 4:
        break
    else:
        print("Computer:", num_to_sign(computer))
        print("You:", num_to_sign(ask))
        if (ask == 2 and computer == 1) or (ask == 3 and computer == 2) or (ask == 1 and computer == 3):
            print("You Won!")
            human_ws += 1
        elif (ask == 1 and computer == 2) or (ask == 2 and computer == 3) or (ask == 3 and computer == 1):
            print("You Lost!")
            python_ws += 1
        elif ask == computer:
            print("Draw")
            draws += 1
        else:
            print("Enter a a number")
            continue

print("Wins:", human_ws, "\nDraws:", draws, "\nLosses:", python_ws)






