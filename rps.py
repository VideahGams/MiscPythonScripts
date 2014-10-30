#-------------------------------
# Rock Paper Scissors in Python
#-------------------------------
import random

isRunning = True

moves = ["rock", "paper", "scissors"]

commands = ["? or help", "scores", "quit"]

playerScore = 0
cpuScore = 0

print("\n")
print("-----------------------------------------")
print("Rock Paper Scissors")
print("Made by Ruairidh Carmichael to learn more Python")
print("-----------------------------------------\n")

print("Enter your move!")
print("Type ? for help.")

def printScores():
	print("\nThe current scores are: ")
	print("Player: " + str(playerScore))
	print("Computer: " + str(cpuScore))

def executeGame(inputedmove):

	global playerScore
	global cpuScore

	cpuChoice = random.randrange(0, len(moves))
	
	print("You have inputed the move: " + moves[inputedmove].capitalize() + ".\n")

	print("The computer has inputed the move: " + moves[cpuChoice].capitalize() + ".\n")


	#Ugh, messy.
	if cpuChoice == 0 and inputedmove == 1:
		print("You win this round!")
		playerScore += 1

	elif cpuChoice == 1 and inputedmove == 2:
		print("You win this round!")
		playerScore += 1

	elif cpuChoice == 2 and inputedmove == 0:
		print("You win this round!")
		playerScore += 1

	elif cpuChoice == inputedmove:
		print("The round ended in a draw.")

	else:
		print("You lost this round.")
		cpuScore += 1

	printScores()
	

while isRunning == True:

	playermove = input("\n>")

	if len(playermove) == 0:
		print("ERROR: You didn't enter a move!")
		continue

	if playermove == "?" or playermove == "help":

		print("\nMoves:")

		for x in moves:
			print(x.capitalize())

		print("\nCommands:")

		for x in commands:
			print(x)

	elif playermove == "scores":
		printScores()

	elif playermove == "quit":
		isRunning = False

	else:
		for x in range(len(moves)):
			if playermove.lower() == moves[x]:
				executeGame(x)

