from datetime import datetime
from typing import Sequence, Union

from deck import CardDeck, Hand


class Game:
    def __init__(self, players: Union[int, Sequence[str]] = 2, initial_hand_size=0, sep=None, player_sep=', '):
        self.__game_log = []
        self.round_count = 0
        self.winner = None
        self.__sep = sep
        self.player_sep = player_sep

        self.log("Let's set up.")
        self.draw_pile = CardDeck(name='Deck')
        self.draw_pile.shuffle()
        self.log(self.draw_pile)
        self.players = []

        if isinstance(players, int):
            for _ in range(players):
                self.players.append(Hand(self.draw_pile.draw(initial_hand_size)))
        else:
            for item in players:
                self.players.append(Hand(self.draw_pile.draw(initial_hand_size), name=str(item)))

        self.log(self.display_players)
        self.discard_pile = CardDeck([])
        self.log("And now we're ready to play.")
        self.log_separator()

    def log(self, message=None, color=None):
        if message is not None:
            self.__game_log.append({
                'time': datetime.now(),
                'color': color,
                'message': str(message),
            })
        return self.__game_log

    def log_separator(self):
        if self.__sep is not None:
            self.log(self.__sep)

    @property
    def display_players(self):
        return self.player_sep.join([str(player) for player in self.players])

    def turn(self, player):
        self.log(f"{player.name}'s turn")
        player.receive_card(self.draw_pile.draw())
        self.log(self.draw_pile)
        self.log(self.display_players)

    def round(self):
        self.round_count += 1
        self.log(f'Round {self.round_count}:')
        for p in self.players:
            self.turn(p)
        self.log_separator()

    def determine_winner(self):
        self.log('... and the winner is ...\n...\ndrum roll...')
        scores = [p.value() for p in self.players]
        self.log(scores)
        winning_score = max(scores)
        self.log(f'winning score = {winning_score}')
        winner = self.players[scores.index(winning_score)]
        self.log(f'The winner is player {winner} with the score {winning_score}.')

    @property
    def game_log(self):
        return self.__game_log

    @property
    def display_log(self):
        return self.format_log('t')

    # noinspection PyBroadException
    def format_log(self, log_format='t'):
        try:
            log_format = log_format.lower()
        except Exception:
            log_format = 't'

        if log_format.startswith('h'):
            return 'HTML log formatting not implemented'

        if not log_format or log_format.startswith('t'):
            return '\n'.join([str(log_item['message']) for log_item in self.__game_log])

    def play(self, rounds=3):
        for _ in range(rounds):
            self.round()
        self.log('Game over.')
        self.log(self.draw_pile)
        self.log(self.display_players)

        self.winner = max(self.players)
        self.log(f'The winner is {self.winner.name} with the score {self.winner.value()}.')
        return self.log()


def practice_game():
    game = Game(players=2, initial_hand_size=0, sep=' ')
    game.play(rounds=3)
    print(game.display_log)
    return game


def practice_game2():
    game = Game(players=['Amy', 'Bob', 'Cam'], initial_hand_size=0, sep='')
    game.play(rounds=3)
    print(game.display_log)
    return game


if __name__ == '__main__':
    print('Sample game with two players without names:')
    practice_game()
    print('\n')
    print('Sample game with three named players:')
    practice_game2()
