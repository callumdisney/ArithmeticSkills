import random #Imports random for randint and random.choice
from operator import add, sub, mul #Imports operator support

ListOfOperations = (add, sub, mul) #Creats list of operations (addition, subtraction, multiplication)

Score = 0 #Sets score to 0 so that we can add 1 later on  without having to assign it with confusing code
Name = input("What is your name? ") #Asks user for their name

for i in range (10): #Repeats 10 times
  #Randomly selects 2 numbers between 1 and 10
  Number1, Number2 = random.randint(1, 10), random.randint(1, 10)
  #Randomly selects between add, subtract, and multiply
  Operation = random.choice(ListOfOperations)
  #Works out the answer to the question it will ask
  Answer = Operation (Number1, Number2)
  #Converts operation to str so that it can be used easier later
  Operation = str(Operation)
  #Changes operation text so it can be displayed in more user-friendly way
  if Operation == "<built-in function add>": #Addition
    Operation = "+"
  if Operation == "<built-in function sub>": #Subtraction
    Operation = "-"
  if Operation == "<built-in function mul>": #Multiplication
    Operation = "*"

  UserAnswer = int(input("What is " + str(Number1) + " " + Operation + " " + str(Number2) + "? ")) #Asks the user the random question (with the 2 random numbers and random operation)
  if UserAnswer == Answer: #If user answers correctly, tell them, and add 1 to their score
    print ("Correct!")
    Score = Score + 1
  else: #If user answers incorrectly, tell them, and leave the score as it is
    print ("Incorrect.")
print ("Done! Your score: " + str(Score)) #Once the user has completed all 10 questions, tell them, and output their final score 
with open("results.txt", "a") as f: #Appends user's name and score to text file
  f.write("Name: " + Name + "\nScore: " + str(Score) + "\n\n")
