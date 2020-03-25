import random

from card import Card


class CardList:
    def __init__(self, card_list=None, name=''):
        self.name = name
        if card_list:
            self._cards = [card for card in card_list if isinstance(card, Card)]
            if len(self._cards) != len(card_list):
                raise TypeError('List of cards expected. This was passed:{}')
        else:
            self._cards = []

    def __repr__(self):
        name = f'{self.name}:' if self.name else ''
        return f'{name}{str(self._cards)}'

    def __str__(self):
        name = f'{self.name}:' if self.name else ''
        return f'{name}{str([str(card) for card in self._cards])}'

    def __len__(self):
        return len(self._cards)

    def __bool__(self):
        return bool(self._cards)

    def is_empty(self):
        return not self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def sort(self, color_order=None):
        Card.set_color_order(color_order)
        self._cards.sort()

    def __gt__(self, other):
        return self.value() > other.value()

    def value(self):
        return sum([card.card_value() for card in self._cards])

    def receive_card(self, card):
        self._cards.append(card)
        self.sort()


class CardDeck(CardList):
    def __init__(self, card_list=None, decks=1, name=''):
        if card_list is None:
            card_list = []
            for _ in range(decks):
                card_list.extend(Card.full_deck())
        super().__init__(card_list, name=name)

    def draw(self, number=None):
        if number is None:
            try:
                return self._cards.pop()
            except IndexError:
                raise IndexError('Attempted to draw from empty deck')
        return [self.draw() for _ in range(min(number, len(self)))]

    def top(self):
        try:
            return self._cards[-1]
        except IndexError:
            return None


class Hand(CardList):
    count = 0

    def __init__(self, *args, **kwargs):
        Hand.count += 1
        super().__init__(*args,
                         name=kwargs.pop('name', f'Player_{Hand.count}'),
                         **kwargs,
                         )
        self.sort()


if __name__ == '__main__':
    deck = CardDeck()
    print(f'initial:  {deck}')
    deck.shuffle()
    print(f'shuffled: {deck}')
    deck.sort(['red'])
    print(f'red-sort: {deck}')
    deck.sort(['yellow', 'green', 'red'])
    print(f'ygr-sort: {deck}')
    deck.shuffle()
    print(f'shuffled: {deck}')
    print(f'top card: {deck.top()}')
    print(f'aftr top: {deck}')
    print(f'drawn crd:{deck.draw()}')
    print(f'aftr draw:{deck}')
    for number in [6, 7, 0, -1, 10, 20]:
        hand = deck.draw(number)
        print(f'hand of {number}:{hand}')
        print(f'aftr drw{number}:{deck}')
    # print(f'top card: {deck.top()}')
    print(f'aftr top: {deck}')
    print(f'drawn crd:{deck.draw()}')
    print(f'aftr draw:{deck}')
    print(f'')
