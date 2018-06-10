import pytest
from worldcup import Group

TEAMS = ['France', 'Australia', 'Peru', 'Denmark']


@pytest.fixture
def group_c_2018():
    """Return the group C of World Cup 2018."""
    return Group('C', TEAMS)


def test_creation(group_c_2018):
    """Test group creation."""
    team_presence = [team in group_c_2018.teams for team in TEAMS]
    assert (
        group_c_2018.id == 'C'
        and False not in team_presence
    )


def test_initialize_games(group_c_2018):
    """Test games initialization."""
    game_1 = group_c_2018.games[0]
    assert (
        len(group_c_2018.games) == 6
        and game_1.team_1 == 'France'
        and game_1.team_2 == 'Australia'
    )


def test_play(group_c_2018):
    """Test play all the group's games, using random predictor."""
    group_c_2018.play()
    assert group_c_2018.games[0].score == (3, 0)


def test_get_rankings(group_c_2018):
    """Test the rankings method."""
    group_c_2018.play()
    rankings = group_c_2018.get_rankings()
    assert (
        len(rankings) == 4
        and rankings[0] == ('France', 6)
        and rankings[1] == ('Australia', 4)
        and rankings[2] == ('Peru', 2)
        and rankings[3] == ('Denmark', 0)
    )
