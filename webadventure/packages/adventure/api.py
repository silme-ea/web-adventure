from .game import Game


def load_advent_dat(data):
    import os
    from .data import parse

    datapath = os.path.join(os.path.dirname(__file__), 'advent.dat')
    with open(datapath, 'r', encoding='ascii') as datafile:
        parse(data, datafile)


def start_new_game():
    game = Game()
    load_advent_dat(game)
    game.start()
    return game


def get_last_output(game):
    return game.output


def do_command(game, command):
    """Take input from submit form of user/prompt.html page and pass it to game instance.
        :param game: instance of Game class
        :param command: string data from submit form of prompt.html page
    """
    import re
    words = re.findall(r'\w+', command)
    if words:
        return game.do_command(words)


class Score:
    def __init__(self):
        self.current_score = 0
        self.max_score = 0


def get_current_score(game):
    score = Score()
    score.current_score, score.max_score = game.compute_score()
    return score


def load_last_game(savefile):
    from os import path
    game = Game.resume(savefile)
    game.output = 'GAME ' + '\'' + path.basename(savefile) + '\'' + ' RESTORED'
    return game