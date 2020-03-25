from datetime import datetime

from deck import CardDeck, Hand


class Game:
    def __init__(self, players=2, initial_hand_size=0):
        self.__game_log = []
        self.round_count = 0
        self.log("Let's set up.")
        self.draw_pile = CardDeck(name='Deck')
        self.draw_pile.shuffle()
        self.log(self.draw_pile)
        self.players = []
        for _ in range(players):
            self.players.append(Hand(self.draw_pile.draw(initial_hand_size)))
        self.log(self.players)
        self.discard_pile = CardDeck([])
        self.log("And now we're ready to play.")

    def log(self, message='', color=None):
        if message:
            self.__game_log.append({
                'time': datetime.now(),
                'color': color,
                'message': message,
            })
        return self.__game_log

    def turn(self, player):
        self.log(f"{player.name}'s turn")
        player.receive_card(self.draw_pile.draw())
        self.log(self.draw_pile)
        self.log(self.players)

    def round(self):
        self.round_count += 1
        self.log(f'Round {self.round_count}:')
        for p in self.players:
            self.turn(p)

    def determine_winner(self):
        self.log('... and the winner is ...\n...\ndrum roll...')
        scores = [p.value() for p in self.players]
        self.log(scores)
        winning_score = max(scores)
        self.log(f'winning score = {winning_score}')
        winner = self.players[scores.index(winning_score)]
        self.log(f'The winner is player {winner} with the score {winning_score}.')

    def play(self, rounds=3):
        for _ in range(rounds):
            self.round()
        self.log('Game over.')
        self.log(self.draw_pile)
        self.log(self.players)

        self.winner = max(self.players)
        self.log(f'The winner is {self.winner.name} with the score {self.winner.value()}.')
        return self.log()


def practice_game():
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


if __name__ == '__main__':
    game = Game(players=2, initial_hand_size=0)
    log = game.play(rounds=3)
