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
