class Player:
    def __init__(self, cards):
        self.cards = list(cards)
    
    def empty_deck(self):
        if len(self.cards) == 0:
            return True
        else:
            return False
    
    def play_card(self):
        card = self.cards.pop(0)
        self.decksize = len(self.cards)
        return card
    
    def add_cards(self, pair):
        for card in pair:
            self.cards.append(card)
    
    def score(self):
        self.cards = self.cards[::-1]
        score = 0
        for i, c in enumerate(self.cards):
            score += (i+1) * c
        return score

    def card_order(self):
        cardstr = ""
        for card in self.cards:
            cardstr += str(card) + ","
        cardstr = cardstr.strip(",")
        return cardstr
    
def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().split("\n\n")
    file.close()
    return inputs

def formatdata():
    global players
    players = []
    for i in inputs:
        i = i.split("\n")
        players.append([int(card.strip()) for card in i[1:]])

def play_Combat():
    p1 = Players[0]
    p2 = Players[1]
    while not (p1.empty_deck() or p2.empty_deck()):
        p1card = p1.play_card()
        p2card = p2.play_card()
        if p1card > p2card:
            pair = [p1card, p2card]
            p1.add_cards(pair)
        else:
            pair = [p2card, p1card]
            p2.add_cards(pair)
    if p2.empty_deck():
        print("Game Over")
        print("Player 1 has won with a score of", p1.score())
    elif p1.empty_deck():
        print("Game Over") 
        print("Player 2 has won with a score of", p2.score())

def Recursive_Combat(players):
    p1 = players[0]
    p2 = players[1]
    playset = {(p1.card_order(), p2.card_order())}
    while not (p1.empty_deck() or p2.empty_deck()):
        #print("Player 1's deck =", p1.cards)
        #print("Player 2's deck =", p2.cards)
        p1card = p1.play_card()
        p2card = p2.play_card()
        #print("Player 1 plays =", p1card)
        #print("Player 2 plays =", p2card)
        if p1card <= p1.decksize and p2card <= p2.decksize:
            p1subdeck = list(p1.cards[0:p1card])
            p2subdeck = list(p2.cards[0:p2card])
            newplayers = [p1subdeck, p2subdeck]
            NewPlayers = [Player(p) for p in newplayers]
            result, _ = Recursive_Combat(NewPlayers)
            if result == 1:
                pair = [p1card, p2card]
                p1.add_cards(pair)
            elif result == 2:
                pair = [p2card, p1card]
                p2.add_cards(pair)
        else:
            if p1card > p2card:
                pair = [p1card, p2card]
                p1.add_cards(pair)
            else:
                pair = [p2card, p1card]
                p2.add_cards(pair)
        if (p1.card_order(), p2.card_order()) in playset:
            return 1, p1.score()
        else:
            playset.add((p1.card_order(), p2.card_order()))
    if p2.empty_deck():
        return 1, p1.score()
    elif p1.empty_deck():
        return 2, p2.score()    

day = 22
inputs = open_file()

formatdata()
Players = [Player(p) for p in players]
play_Combat()
Players = [Player(p) for p in players]
p, score = Recursive_Combat(Players)
print(f"Player {p} has won with a score of {score}" )