from abc import ABCMeta, abstractmethod
import numpy as np
import pandas as pd


class BaseGamePredictor(metaclass=ABCMeta):
    """Predict a game result given two teams."""

    @abstractmethod
    def __init__(self):
        """Initialize a GamePredictor object."""

    @abstractmethod
    def predict_game(self, game):
        """Predict a game result."""


class RandomGamePredictor(BaseGamePredictor):
    """Predict randomly a game."""

    def __init__(self, seed=None):
        """Initialize a random game predictor."""
        np.random.seed(seed)

    def predict_game(self, game):
        """Predict randomly a game with a max number of goals of 5."""
        score = (np.random.randint(0, 5), np.random.randint(0, 5))
        return score


class HistoricalGamePredictor(BaseGamePredictor):
    """Predict deterministically a game based on historical game results."""

    def __init__(self, historical_results_file):
        """Initialize a predictor from an historical result file."""
        self.results = pd.read_csv(historical_results_file)

    def predict_game(self, game):
        """Predict the score of the last game between team 1 and team 2."""
        team_1 = game.team_1
        team_2 = game.team_2
        df = self.results

        def x_team(team):
            return (df.home_team == team) | (df.away_team == team)

        all_games = df[x_team(team_1) & x_team(team_2)].sort_values(
            by='date', ascending=False)

        if not all_games.empty:
            last_game = all_games.iloc[0]
            if last_game.home_team == team_1:
                score = (last_game.home_score, last_game.away_score)
            elif last_game.home_team == team_2:
                score = (last_game.away_score, last_game.home_score)
        else:  # Some teams might have never played against each other
            score = (0, 0)

        return score


class EloRatingGamePredictor(BaseGamePredictor):
    """Predict score on Elo rating win expectancy and WC average stats."""

    def __init__(self):
        """Initialize an Elo ratings based predictor."""
        pass

    def predict_game(self, game):
        """Predict score based on win expectancy implied by Elo ratings."""
        we = game.win_expectancy()
        if we > 0.75:
            score = (3, 0)
        elif we > 0.5:
            score = (2, 1)
        elif we > 0.25:
            score = (1, 2)
        else:
            score = (0, 3)
        return score
