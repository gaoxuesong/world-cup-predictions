import pytest
from worldcup import WorldCup
from gamepredictor import HistoricalGamePredictor


@pytest.fixture
def worldcup_2018():
    """Return 2018 World Cup with historical game predictions."""
    historical_gp = HistoricalGamePredictor("results.csv")
    wc = WorldCup("groups.csv")
    wc.play(historical_gp)
    return wc


def test_creation(worldcup_2018):
    """Test the object creation with historical game predictor."""
    assert worldcup_2018


def test_play(worldcup_2018):
    """Test that all the group games can be played and predicted."""
    assert worldcup_2018
