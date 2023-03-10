from random import randint, choice #For random numbers and choices
from operator import add, sub, mul #For operators

listOfoperations = (add, sub, mul) #Creats list of operations (addition, subtraction, multiplication)

score = 0 #Sets score to 0 to start

playAgain = True #Sets playAgain to True to start so game runs

while playAgain == True:
  
  input("Hello! This little quiz will ask you mathematics questions. Ready? (Press enter to start) ") #Greets user and asks them to press enter to start

  #Starter questions
  name = (input("\nFirst of all, what is your name? ")).capitalize() #Asks user for their name
  numAllowed = False #For repeating question if error caught
  while numAllowed == False:
    try:
      questionNum = int(input("\nHow many questions would you like? "))
    except ValueError: #Catches if float or string given
      print("\nMust be a whole number!\n")
    else:
      numAllowed = True
      print (f"\nOkay, {questionNum} questions it is!")
  numAllowed = False #For repeating question if error caught
  while numAllowed == False:
    try:
      betweenFirst = int(input("\nWhat should the numbers within the questions be between? Enter the first number: "))
    except ValueError: #Catches if float or string given
      print("\nMust be a whole number!")
    else:
      numAllowed = True
  numAllowed = False #For repeating question if error caught
  while numAllowed == False:
    try:
      betweenSecond = int(input("\nWhat should the numbers within the questions be between? Enter the second number: ")) #Gets the number of questions the user wants (min 5)
    except ValueError: #Catches if float or string given
      print("\nMust be a whole number!")
    else:
      numAllowed = True

  #Actual quiz
  for i in range (questionNum): #Repeats number of times specified by user
    #Randomly selects 2 numbers between the user's specified numbers
    Number1, Number2 = randint(betweenFirst, betweenSecond), randint(betweenFirst, betweenSecond)
    #Randomly selects between add, subtract, and multiply
    operation = choice(listOfoperations)
    #Works out the answer to the question it will ask
    answer = operation(Number1, Number2)
    #Converts operation to str so that it can be used easier later
    operation = str(operation)
    #Changes operation text so it can be displayed in more user-friendly way
    if operation == "<built-in function add>": #Addition
      operation = "+"
    if operation == "<built-in function sub>": #Subtraction
      operation = "-"
    if operation == "<built-in function mul>": #Multiplication
      operation = "*"
    
    userAnswerAllowed = False
    while userAnswerAllowed == False:
      try:
        userAnswer = float(input(f"\nWhat is {str(Number1)} {operation} {str(Number2)}? ")) #Asks the user the random question (with the 2 random numbers and random operation)
        if userAnswer == answer: #If user answers correctly, tell them, and add 1 to their score
          userAnswerAllowed = True
          print ("That's correct!")
          score += 1
        else: #If user answers incorrectly, tell them the correct answer, and leave the score as it is
          userAnswerAllowed = True
          print (f"That is incorrect. The correct answer is {answer}.")
      except ValueError: #Catches strings
        print ("Must be a number!")
  print (f"\nDone! Your score is {str(score)}/{str(questionNum)}, and has been saved to the log file.") #Once the user has completed all questions, tell them, and output their final score

  #Appends user's name and score to text file
  with open("results.txt", "a") as f:
    f.write(f"Name: {name}\nNumbers: {str(betweenFirst)}-{str(betweenSecond)}\nScore: {str(score)}/{str(questionNum)}\n\n")

  #Play again?
  playAgainQ = ""
  playAgainQ = input("\nWould you like to play again? (Y)es or (N)o: ")
  playAgainQ = playAgainQ.capitalize()
  while playAgainQ not in ["Y", "N", "Yes", "No"]:
    playAgainQ = input("\nWould you like to play again? (Y)es or (N)o: ")
    playAgainQ = playAgainQ.capitalize()
  if playAgainQ in ["Y", "Yes"]:
    playAgain = True
  if playAgainQ in ["N", "No"]:
    playAgain = False
    print ("Bye!")
