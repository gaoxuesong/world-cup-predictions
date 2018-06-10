from abc import ABCMeta, abstractmethod
import numpy as np


class BaseGamePredictor(metaclass=ABCMeta):
    """Predict a game result given two teams."""

    @abstractmethod
    def __init__(self):
        """Initialize a GamePredictor object."""

    @abstractmethod
    def predict_game(self, team_1, team_2):
        """Predict a game result."""


class RandomGamePredictor(BaseGamePredictor):
    """Predict randomly a game."""

    def __init__(self, seed=None):
        """Initialize a random game predictor."""
        np.random.seed(seed)

    def predict_game(self, team_1, team_2):
        """Predict randomly a game with a max number of goals of 5."""
        score = (np.random.randint(0, 5), np.random.randint(0, 5))
        return score
