import pytest
from worldcup import WorldCup
from gamepredictor import EloRatingGamePredictor


@pytest.fixture
def worldcup_2018():
    """Return 2018 World Cup with historical game predictions."""
    elo_gp = EloRatingGamePredictor()
    wc = WorldCup("groups.csv")
    wc.play(elo_gp)
    return wc


def test_creation(worldcup_2018):
    """Test the object creation with historical game predictor."""
    assert worldcup_2018


def test_predict_score(worldcup_2018):
    """Test that predicted score is from latest historical game."""
    g = worldcup_2018.get_game("France", "Denmark")
    assert g.score == (2, 1)
