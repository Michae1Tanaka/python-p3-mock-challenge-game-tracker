class Result:
    all = []

    def __init__(self, player, game, score):
        if isinstance(player, Player) and isinstance(game, Game):
            self._player = player
            self._game = game
            player.results(self)
            game.results(self)
            game.players(player)
        else:
            raise Exception(
                "player and game must be instances of Player class and Game class respectively."
            )
        if isinstance(score, int) and 0 < score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be in between 0 snd 5001")
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if 0 < new_score <= 5000:
            self._score = new_score
        else:
            raise Exception("Score must be in between 0 and 5001")

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game


from classes.game import Game
from classes.player import Player
