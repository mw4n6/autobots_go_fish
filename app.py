from .classes.deck import Deck
from .classes.player import Player
from .classes.computer import Computer


class GameManager:
    """
    Handles logic for creating and running
    a game of go fish
    """

    def __init__(self):
        self.deck = Deck()
        self.players = []
        first_hand = [Deck.draw() for _ in xrange(7)]
        second_hand = [Deck.draw() for _ in xrange(7)]
        self.players.append(Player(first_hand))
        self.players.append(Computer(second_hand))
        self.playGame()

    def playGame(self):
        active_player = 0
        while not (deck.isEmpty() and players[0].hand.isEmpty() and players[1].hand.isEmpty()):
            request = self.players[active_player].getRequest()
            new_card = self.players[(active_player+1) % 2].reply_to_fish(request)
            if new_card is None:
                new_card = self.deck.draw()
                replay = new_card == request
            self.players[active_player].addCard(new_card)
            active_player = (active_player+1) % 2 if not replay else active_player
        self.reportResults()

    def reportResults(self):
        winner, loser = (0, 1) if self.player[0].numPairs() > self.player[1].numPairs() else (1, 0)
        print self.players[winner], 'wins'
        print self.players[loser], 'wins'


if __name__ == '__main__':
    gm = GameManager()
