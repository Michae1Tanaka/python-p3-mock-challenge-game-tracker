class Player:
    all_players = []

    def __init__(self, username):
        if 2 <= len(username) <= 16 and isinstance(username, str):
            self._username = username
            self._results = []
            Player.all_players.append(self)
        else:
            raise Exception(
                "Username must be more than 1 character and less than 17 characters."
            )

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str):
            self._username = new_username
        else:
            raise Exception("Username must be a string.")

    def results(self, new_result=None):
        if new_result:
            self._results.append(new_result)
        return self._results

    def games_played(self):
        return list(set([result.game for result in self._results]))

    def played_game(self, game):
        for result in self._results:
            if game == result.game:
                return True
        else:
            return False

    def num_times_played(self, game):
        return len([result for result in self._results if game == result.game])

    @classmethod
    def highest_scored(cls, game):
        highest_avg_score = -1
        highest_avg_player = None
        for player in cls.all_players:
            avg_score = game.average_score(player)
            if avg_score > highest_avg_score:
                highest_avg_score = avg_score
                highest_avg_player = player
        return highest_avg_player


from classes.result import Result
