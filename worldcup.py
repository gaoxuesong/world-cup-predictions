import pandas as pd
import numpy as np
import itertools
import operator


def WorldCup(object):
    """World cup object."""

    def __init__(self, filename):
        """Initalize world cup with a file containing groups and teams."""
        df = pd.read_csv(filename, index_col='Group')
        group_ids = 'ABCDEFG'
        print("test")
        for gid in group_ids:
            print(gid)
            print(df[gid].values)


class Group(object):
    """Represents a world cup group."""

    def __init__(self, id, teams):
        """Initialize a group."""
        self.id = id
        self.teams = teams
        self.games = []
        self.initialize_games()

    def initialize_games(self):
        """Initialize all the games of the group."""
        for (team_1, team_2) in itertools.combinations(self.teams, 2):
            self.games.append(Game(team_1, team_2))

    def play_all_games(self):
        """Play all the games of the group."""
        for g in self.games:
            g.play()

    def get_rankings(self):
        """Return the rankings of the group."""
        n = len(self.teams)
        points = dict(zip(self.teams, np.zeros(n)))
        for g in self.games:
            t1, t2 = g.get_teams()
            pts1, pts2 = g.get_points()
            points[t1] += pts1
            points[t2] += pts2
        rankings = sorted(points.items(),
                          key=operator.itemgetter(1),
                          reverse=True)
        return rankings


class Game(object):
    """Represents a world cup game, either in group or knockout stage."""

    def __init__(self, team_1, team_2):
        """Initialize a game."""
        self.team_1 = team_1
        self.team_2 = team_2
        self.score = (0, 0)

    def get_teams(self):
        """Return a tuple of the two teams."""
        return (self.team_1, self.team_2)

    def play(self):
        """Play a game and record the score."""
        self.score = (np.random.randint(0, 5), np.random.randint(0, 5))

    def get_points(self):
        """Return the points gained by each team."""
        s = self.score
        if s[0] == s[1]:  # This is a draw
            return (1, 1)
        elif s[0] > s[1]:  # Team 1 wins
            return (2, 0)
        elif s[0] < s[1]:  # Team 2 wins
            return (0, 2)
