import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spade", "Club", "Hearts", "Diamond"]:
            for v in range(1, 14):
                if v == 10:
                    v = "J"
                if v == 11:
                    v = "Q"
                if v == 12:
                    v = "K"
                if v == 13:
                    v = "A"
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        self.shuffle()
        random.choice(self.cards).show()

    def show(self):
        for i in self.cards:
            i.show()


deck = Deck()
# deck.shuffle()
# deck.show()
deck.draw()
deck.draw()
deck.draw()
deck.draw()