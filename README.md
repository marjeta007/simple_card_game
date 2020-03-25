# simple_card_game

Language: Python 3.8+

## Challenge Description:

Create a card game which supports 3 of the operations below. 

1. Shuffle cards in the deck: randomly mix the cards in the card deck,
and return a whole deck of cards with a mixed order 

2. Get a card from the top of the deck: get one card from top of the
card deck, return a card, and if there is no card left in the deck
return error or exception.  

3. Sort cards: take a list of color as parameter and sort the card
in that color order. Numbers should be in ascending order.  
i.e. If the deck has a card contains with following order

      `(red, 1), (green, 5), (red, 0), (yellow, 3), (green, 2)`

   then
 
     `Sort cards([yellow, green, red])`
 
   will return the cards with following order:
     
       `(yellow, 3), (green, 0), (green, 5), (red, 0), (red, 1)` 

4. Determine winners:

   2 players play the game.
   
   They will draw 3 cards by taking turns. 

   Whoever has the high score wins the game.
   
   Color point calculation:

      `red = 3,
      yellow = 2,
      green = 1`
      
   The point is calculated by `color point * number` in the card.   
  
## Design

#### Card

Class `Card` instances represent single cards.
Instances have the properties, `color` and `number`.

There are class properties that enforce game restrictions:
`color_list` (list of available colors) and
`number_list` (list of available numbers).
Attempting to create a `Card` with a color that's not in `color_list` 
or `number` that's not in `number_list` raises `ValueError`.

Operators `>` and `<` can be used for sorting cards by
color and then by number.

Class methods: 

`full_deck` generates a list of cards
representing all possible legal color-number combinations.

`set_color_order` changes the order of colors for operators `>` and `<`.
If colors are missing in the argument, those colors are added at the
end, in their previous order.

#### CardDeck

Class `CardDeck` can be used as a draw pile or discard pile of cards.

Method `draw` removes the top card and returns it. If the deck is empty,
it raises `IndexError`.

Method `top` returns the top card, but it doesn't remove it from the deck.
This allows for peeking at the top card without removing it.
If deck is empty, it returns `None`.

Constructor uses either argument `card_list` to create a deck with
specific cards, or `decks`, a number representing the number of full
sets of all available cards, by default `1`.

#### Hand

Class `Hand` represents a player hand. Player has a `name`
and a list of cards.
If `name` is not provided, `Player_<number>` is used, using
consecutive numbers.
Each player's cards are automatically ordered whenever the player
receives another card.
 
#### CardList
 
Class `CardList` is a superclass of `CardDeck` and `Hand`
and provides common functionality:
property `_cards` and the following methods `shuffle`, `sort`,
`is_empty` (returns `True` if list of cards is empty and `False`
otherwise),
`value` (returns the sum of values of all cards in the list),
and `receive_card`.

It also provides support for functions `len()`, `repr()`,
converting to `str` or `bool` (`False` if empty, `True` otherwise),
and comparison with `<` and `>` based on the `value` method.

#### Game

Class `Game` represents a simple card game. The game has a
draw pile and discard pile (both instances of `CardDeck`) and a
list of players.

Constructor argument `players` can either be
a number (the game will have that many anonymous players),
or a list of names. The argument `initial_hand_size` (0 by default)
can be used to set the initial hand size of the players.

The following methods are available:

`turn` represents a turn for one player. In the current version
this just means that the player draws a card.

`round` gives each player a turn and keeps track of the number of
rounds.

`play` takes a number of rounds (3 by default) and provides that
many rounds.
After these rounds are complete, it determines the winner.

The game keeps a log of the game progress.
Property `display_log` converts the log to text, separating log items
by newline characters. Property `game_log` returns unformatted log.
