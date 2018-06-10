import pytest
from worldcup import Group

TEAMS = ['France', 'Australia', 'Peru', 'Denmark']


@pytest.fixture
def group_example():
    return Group('C', TEAMS)


def test_creation(group_example):
    team_presence = [team in group_example.teams for team in TEAMS]
    assert (
        group_example.id == 'C'
        and False not in team_presence
    )


def test_initialize_games(group_example):
    game_1 = group_example.games[0]
    assert (
        len(group_example.games) == 6
        and game_1.team_1 == 'France'
        and game_1.team_2 == 'Australia'
    )


def test_play(group_example):
    group_example.play()
    assert group_example.games[0].score


def test_get_rankings(group_example):
    rankings = group_example.get_rankings()
    assert len(rankings) == 4
