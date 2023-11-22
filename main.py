import random
class Player:
    def __init__(self, playerName):
        self.name = playerName
        self.score = 0

    @property
    def getPlayerName(self):
        return self.name
    @property
    def GetPlayerScore(self):
        return self.score

    def SetPlayerScore(self, score):
        self.score = score

def Game(Player1, Player2):
    print("Rock Paper Scissors Game Starting...\n")
    gameWinnerName = None

    while True:
        print("New Round...")
        if Player1.score == 3 or Player2.score ==3:
            if Player1.score == 3:
                gameWinnerName = Player1.getPlayerName
            else:
                gameWinnerName = Player2.getPlayerName
            break
        else:
            player1Input = input(f"{Player1.getPlayerName} -> Choose your option: (rock, paper, scissors)\n")
            player2Input = input(f"{Player2.getPlayerName} -> Choose your option: (rock, paper, scissors)\n")

            if player1Input == player2Input:
                print("Draw")
            elif  player1Input == "rock" and player2Input == "paper":
                print("\nPlayer 2 Won!")
                print(f"Player Moves: \n{Player1.getPlayerName}: {player1Input}\n{Player2.getPlayerName}: {player2Input}")
                Player2.score += 1

            elif  player1Input == "rock" and player2Input == "scissors":
                print("\nPlayer 1 Won!")
                print(f"Player Moves: \n{Player1.getPlayerName}: {player1Input}\n{Player2.getPlayerName}: {player2Input}")
                Player1.score += 1

            elif  player1Input == "paper" and player2Input == "rock":
                print("\nPlayer 1 Won!")
                print(f"Player Moves: \n{Player1.getPlayerName}: {player1Input}\n{Player2.getPlayerName}: {player2Input}")
                Player1.score += 1

            elif  player1Input == "paper" and player2Input == "scissors":
                print("\nPlayer 2 Won!")
                print(f"Player Moves: \n{Player1.getPlayerName}: {player1Input}\n{Player2.getPlayerName}: {player2Input}")
                Player2.score += 1

            elif  player1Input == "scissors" and player2Input == "rock":
                print("\nPlayer 2 Won!")
                print(f"Player Moves: \n{Player1.getPlayerName}: {player1Input}\n{Player2.getPlayerName}: {player2Input}")
                Player2.score += 1

            elif  player1Input == "scissors" and player2Input == "paper":
                print("\nPlayer 1 Won!")
                print(f"Player Moves: \n{Player1.getPlayerName}: {player1Input}\n{Player2.getPlayerName}: {player2Input}")
                Player1.score += 1

            else:
                print("Invalid Options, Make sure you chose either rock, paper or scissors.")

    print(f"Game Completed.\nWinner is {gameWinnerName}")
bob = Player("Bob")
jack = Player("Jack")

Game(bob, jack)
