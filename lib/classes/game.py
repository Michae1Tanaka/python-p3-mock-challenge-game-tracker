class Game:
    def __init__(self, title):
        if len(title) == 0:
            raise Exception("Title should have a length of more than 0 characters.")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            raise Exception("Title cannot be changed once initialized.")
        self._title = new_title

    def results(self, new_result=None):
        if new_result:
            self._results.append(new_result)
        return self._results

    def players(self, new_player=None):
        return list(set([result.player for result in self._results]))

    def average_score(self, player):
        total_score = [
            result.score for result in self._results if result.player == player
        ]
        if len(total_score) == 0:
            return 0
        average_score = sum(total_score) / len(total_score)
        return average_score


from classes.result import Result
