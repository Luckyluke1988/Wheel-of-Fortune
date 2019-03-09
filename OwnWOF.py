class WOFPlayer:

    def __init__(self,name,prizeMoney=0):
        self.name = name
        self.prizeMoney = prizeMoney

    def addprizeMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt

    def getBankrupt(self):
        self.prizeMoney = self.prizemoney = 0

    def __str__(self):
        return "This is one instance of WOFPlayer with the name:{} and has ${} Prize Money".format(self.name,self.prizeMoney)


def checkMatch(phrase,gussed):
    result = ""
    for letter in phrase:
        if letter in guessed:
            result = result + letter
        if letter == " ":
            result = result + " "
        else:
            result = result + "_"
    return result


num_human_str = input('How many human players?')
num_human = int(num_human_str)

human_players = [WOFPlayer(input('Enter the name for player #{}'.format(i+1))) for i in range(num_human)]
players = human_players

guessed = []
playerIndex = 0
phrase = "Hello World"
result = ""


while True:
    player = players[playerIndex]

    guess = input("Player {} please enter a letter or a Phrase".format(player.name))
    guessed.append(guess)
    
    print(checkMatch(phrase,guessed))

    if guess == phrase:
        winner = player
        print("the Winner is".format(player.name))
        break

    
    playerIndex = (playerIndex + 1) % len(players)

