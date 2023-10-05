import sys, random

scorePlayer = 0
scoreComputer = 0
scoreTies = 0

while True:
    print('Wins: ' + str(scorePlayer) + ' Loses: ' + str(scoreComputer) + ' Ties: ' + str(scoreTies))

    print('Please enter "rock" "paper" or "scissors" or the first letter.')
    guess = input()
    guessNum = 0
    if guess == 'rock' or guess == 'r':
        guessNum = 1
    elif guess == 'paper' or guess == 'p':
        guessNum = 2
    elif guess == 'scissors' or guess == 's':
        guessNum = 3
    elif guess == 'exit':
            sys.exit()
    else:
        print('Your input is invalid.')
        continue


    compGuessNum = random.randint(1,3)
    compGuess = ''
    if compGuessNum == 1:
        compGuess = 'rock'
    elif compGuessNum == 2:
        compGuess = 'paper'
    elif compGuessNum == 3:
        compGuess = 'scissors'
    print('The computer threw down ' + compGuess)


    if compGuessNum == guessNum:
        print('No winner.')
        scoreTies = scoreTies + 1
    elif (compGuessNum == 1 and guessNum == 2) or (compGuessNum == 2 and guessNum == 3) or (compGuessNum == 3 and guessNum == 1):
        print('You win!')
        scorePlayer = scorePlayer + 1
    else:
        print ('You lose.')
        scoreComputer = scoreComputer + 1


    print('Try again')



















