import collections

class CardSet:

    def __init__(self, numCardsInSet):
        self.numCardsInSet = numCardsInSet
        self.cards = list()

    def addCardToSet(self, *cardTuple) -> str:
        self.cards.append(cardTuple)
        return 'Card has been appended to set'

    def removeCardFromSet(self, *cardTuple) -> str:
        self.cards.remove(cardTuple)
        return 'Card has been removed from set'

    def searchForCard(self, *searchCard) -> str:
        ''' Unfinished: must iterate through cards in "cards"
        and compare each one with "searchCard" which is a tuple'''

        return 'Card (is/is not) in the set'
