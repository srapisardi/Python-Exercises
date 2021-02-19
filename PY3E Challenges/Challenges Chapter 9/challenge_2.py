#Challenge 2 Create a War card game

import cards, games

class War_Card(cards.Card):
    def __init__(self, rank, suit):
        super(War_Card,self).__init__(rank,suit)

    @property
    def value_hand(self):
        v = War_Card.RANKS.index(self.rank) + 1
        if v == 1:
            v == 14
        else:
            None
        return v

class War_Deck(cards.Deck):
    def populate(self):
        for rank in War_Card.RANKS:
            for suit in War_Card.SUITS:
                self.cards.append(War_Card(rank,suit))


class War_Hand(cards.Hand):
    def __init__(self,name):
        super(War_Hand,self).__init__()
        self.name = name

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"

        return rep

    def draw(self):
        top_card = self.cards[0]
        self.cards.remove(top_card)
        return top_card

    @property
    def value_hand(self):
        for card in self.cards:
            val = card.value
            return val

class War_Game(object):
    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.player = War_Hand(self.name)
        self.computer = War_Hand("Computer")
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        hands = [self.player,self.computer]
        self.deck.deal(hands,per_hand=26)

        while True:
            input("Press Enter to draw a card")
            your_card = self.player.draw()
            cpu_card = self.computer.draw()
            print(self.player.name,your_card)
            print(self.computer.name,cpu_card)
            if your_card.value_hand() > cpu_card.value_hand():
                print("You win!")
            elif your_card.value_hand() < cpu_card.value_hand():
                print("You lose!")
            else:
                print("It's a tie!")


            if len(self.computer.cards) == 0 and len(self.player.cards) == 0:
                print("Players out of cards.")
                break

game = War_Game()
game.play()
