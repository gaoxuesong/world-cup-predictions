import pytest
from worldcup import Game


@pytest.fixture
def game_example():
    """Return an example of game."""
    return Game('France', 'Peru')


def test_creation(game_example):
    """Test the game creation."""
    assert (
        game_example
        and game_example.team_1 == 'France'
        and game_example.team_2 == 'Peru'
    )


def test_get_teams(game_example):
    """Test the teams attributes of the game object."""
    t1, t2 = game_example.get_teams()
    assert t1 == 'France' and t2 == 'Peru'


def test_play(game_example):
    """Test play the game, using the random predictor."""
    game_example.play()
    assert game_example.score == (3, 0)


def test_get_points(game_example):
    """Test the points counting functionality."""
    # Draw
    game_example.score = (1, 1)
    draw = game_example.get_points()
    # Team 1 wins
    game_example.score = (3, 1)
    t1_win = game_example.get_points()
    # Team 2 wins
    game_example.score = (0, 2)
    t2_win = game_example.get_points()
    assert (
        draw == (1, 1)
        and t1_win == (2, 0)
        and t2_win == (0, 2)
    )


def test_win_expectancy(game_example):
    """Test the game win expectancy."""
    assert game_example.win_expectancy() == pytest.approx(0.60, abs=0.01)


def test_win_expectancy_formatted(game_example):
    """Test the game win expectancy formatted."""
    target_str = "60% France"
    assert game_example.win_expectancy_formatted() == target_str
