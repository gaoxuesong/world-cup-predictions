import pytest
from worldcup import WorldCup


@pytest.fixture
def worldcup_2018():
    """Instantiate a world cup object."""
    return WorldCup("groups.csv")


def test_creation(worldcup_2018):
    """Test the object creation."""
    assert worldcup_2018


def test_has_32_teams(worldcup_2018):
    """Test that 2018 world cup has a total of 32 teams."""
    nb_teams = sum(len(g.teams) for g in worldcup_2018.groups)
    assert nb_teams == 32


def test_get_game(worldcup_2018):
    """Test the game getter."""
    g = worldcup_2018.get_game("Costa Rica", "Brazil")
    assert g.team_1 == "Brazil" and g.team_2 == "Costa Rica"


def test_get_nonexistent_game(worldcup_2018):
    """Test if a non existent game returns None."""
    g = worldcup_2018.get_game("France", "Brazil")
    assert g is None
