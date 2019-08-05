i = 0
while i == 0:

    # Here i ask for the choices from both players
    Player1 = input("What is your choice player1?")
    Player2 = input("What is your choice player2?")
    Player1 = Player1.lower()
    Player2 = Player2.lower()

    # Here i writed the moments where and when is a draw
    if Player1 == Player2:
        print("It's a draw")

    # Here i writed the moments where and when player1 wins
    elif Player1 == "rock" and Player2 == "scissors":
        print("Player 1 wins")
    elif Player1 == "paper" and Player2 == "rock":
        print("Player 1 wins")
    elif Player1 == "scissors" and Player2 == "paper":
        print("Player 1 wins")

    # Here i writed the moments where and when player2 wins
    elif Player1 == "scissors" and Player2 == "rock":
        print("Player 2 wins")
    elif Player1 == "rock" and Player2 == "paper":
        print("Player 2 wins")
    elif Player1 == "paper" and Player2 == "scissors":
        print("Player 2 wins")

    # I write here what happens when you don't write Rock, paper or scissors.
    else:
        print("Woops, it seems that's not Rock, Paper or Scissors")

    # This is the end of the game, somethings
    answer = input("Do you want to start another game? Yes/No: ")
    answer = answer.lower()

    if answer == "yes":
        print("New game starting...")
    elif answer == "no":
        print("Closing game, have a nice day.")
        i = i + 1
    else:
        print("You only have to write Yes/No, try to write it in your next attempt")