#!/usr/bin/env python

"""
AOC 2023: DAY 2

Author: Jennifer Kadowaki
E-mail: jkadowaki@arizona.edu
Last Updated: 2023 Dec 06
"""

import re

################################################################################

def clean_game(game:str) -> (int,list):
    """
    Pre-processes each game (i.e., line of input file)
    INPUT: 'Game 1: 2 red, 2 green; 6 red, 3 green; 2 red, 1 green, 2 blue; 1 red'
    """
    
    # OUTPUT: [ 'Game 1',
    #           '2 red, 2 green',
    #           '6 red, 3 green', 
    #           '2 red, 1 green, 2 blue',
    #           '1 red' ]
    game = re.split(': |; ', game)

    # Game Number
    game_idx  = int( game[0].split()[1] )
    
    # OUTPUT: [ ['2', 'red', '2', 'green'],
    #           ['6', 'red', '3', 'green'],
    #           ['2', 'red', '1', 'green', '2', 'blue'],
    #           ['1', 'red'] ]
    hand_list = [ re.split(', |\s', curr_hand) for curr_hand in game[1:] ]
    
    # OUTPUT: [ {'red': 2, 'green': 2},
    #           {'red': 6, 'green': 3},
    #           {'red': 2, 'green': 1, 'blue': 2},
    #           {'red': 1} ] 
    return game_idx, [{color: int(hand[idx-1]) for idx, color in enumerate(hand) if idx%2==1}
                                               for hand in hand_list  ]

################################################################################

def test_plausibility( draws:list, 
                       max_config={'red':12, 'green':13, 'blue':14} ) -> bool:
    """
    Outputs whether game plausibility given the number of cubes of each color.
    """

    # Checks whether ALL draws in a game yield cube counts lower than the maximum
    # number of cubes for each color.
    return all([ hand[color]<=max_config[color] for hand in draws
                                                for color in hand.keys() ])    

################################################################################

def get_fewest_cubes(draws:list) -> int:
    """
    Returns the product of the minimum number of cubes needed for each color to
    yield a game where all draws are plausible.

    EXAMPLE:
    1: 3b,      4r;  6b,  2g, 1r;  2g           -->  4r,  2g,  6b  ==> 48
    2: 1b, 2g;       4b,  3g, 1r;  1g, 1b       -->  1r,  3g,  4b  ==> 12
    3: 6b, 8g, 20r;  5b, 13g, 4r;  5g,       1r --> 20r, 13g,  6b  ==> 1560
    4: 6b, 1g,  3r;       3g, 6r;  3g, 15b, 14r --> 14r,  3g, 15b  ==> 630
    5: 1b, 3g,  6r;  2b,  2g, 1r                -->  6r,  3g,  2b  ==> 36
    """
    max_cubes = {}
    product   = 1

    # Store the maximum number of cubes observed for each color for each game.
    for hand in draws:
        for color in hand.keys():
            max_cubes[color] = max( hand[color], max_cubes.get(color, 0))

    # Take the product of the minimum number of cubes needed for each color.
    for value in max_cubes.values():
        product *= value

    return product

################################################################################

def sum_games(input_doc, max_config = {'red':12, 'green':13, 'blue':14}):

    sum_idx  = 0
    sum_prod = 0

    with open(input_doc, "r") as f:  
        for line in f:
            game_idx, draws = clean_game(line)
            game_flag       = test_plausibility(draws, max_config=max_config )
            sum_idx  += game_idx * game_flag
            sum_prod += get_fewest_cubes(draws)
    print(sum_idx, sum_prod)
     

################################################################################

if __name__ == '__main__':

    sum_games('input.txt')


