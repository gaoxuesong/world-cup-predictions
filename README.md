# world-cup-predictions
Predict the results of FIFA World Cup 2018 group stage using historical game results.

## Approach

In current version, a super simplistic approach is used: for a given game, if the two teams met before, the score of the most recent game is predicted. If the teams never met, a 0-0 draw is predicted.

In addition, the win expectancy based on Elo Ratings is computed.

## Datasets

The [results.csv](./results.csv) file comes from the [International football results from 1872 to 2018 Kaggle dataset](https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017), courtesy of [Mart Jürisoo](https://www.kaggle.com/martj42).

The [elo_ratings.csv](./elo_ratings.csv) file comes from the [World Football Elo Ratings](eloratings.net) website (eloratings.net), snapshot as of Jun 10, 2018.

## How to use

Just run the script:
```bash
./run.py
```

or use this Python code in your notebook:
```python
from worldcup import WorldCup
from gamepredictor import HistoricalGamePredictor

# Create World Cup 2018 object from groups file
wc_2018 = WorldCup("groups.csv")

# Create game predictor based on historical results
hist_gp = HistoricalGamePredictor("results.csv")

# Run predictions for the group stage
wc_2018.play(hist_gp)

# Print all game predictions
wc_2018.print_game_results()
```

## Predicted results
```
+---------------+
| Group A       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| Russia        | Saudi Arabia  | 2 - 4   | 62% Russia        |
| Russia        | Egypt         | 0 - 0   | 55% Russia        |
| Russia        | Uruguay       | 1 - 1   | 78% Uruguay       |
| Saudi Arabia  | Egypt         | 0 - 1   | 58% Egypt         |
| Saudi Arabia  | Uruguay       | 1 - 1   | 85% Uruguay       |
| Egypt         | Uruguay       | 0 - 2   | 81% Uruguay       |
+---------------+---------------+---------+-------------------+


+---------------+
| Group B       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| Portugal      | Spain         | 0 - 0   | 60% Spain         |
| Portugal      | Morocco       | 1 - 3   | 80% Portugal      |
| Portugal      | Iran          | 2 - 0   | 74% Portugal      |
| Spain         | Morocco       | 3 - 2   | 86% Spain         |
| Spain         | Iran          | 0 - 0   | 81% Spain         |
| Morocco       | Iran          | 1 - 1   | 58% Iran          |
+---------------+---------------+---------+-------------------+


+---------------+
| Group C       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| France        | Australia     | 6 - 0   | 80% France        |
| France        | Peru          | 0 - 1   | 60% France        |
| France        | Denmark       | 2 - 1   | 68% France        |
| Australia     | Peru          | 0 - 0   | 73% Peru          |
| Australia     | Denmark       | 0 - 2   | 66% Denmark       |
| Peru          | Denmark       | 0 - 0   | 58% Peru          |
+---------------+---------------+---------+-------------------+


+---------------+
| Group D       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| Argentina     | Iceland       | 0 - 0   | 78% Argentina     |
| Argentina     | Croatia       | 2 - 1   | 68% Argentina     |
| Argentina     | Nigeria       | 2 - 4   | 85% Argentina     |
| Iceland       | Croatia       | 1 - 0   | 63% Croatia       |
| Iceland       | Nigeria       | 3 - 0   | 62% Iceland       |
| Croatia       | Nigeria       | 0 - 0   | 73% Croatia       |
+---------------+---------------+---------+-------------------+


+---------------+
| Group E       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| Brazil        | Switzerland   | 0 - 1   | 81% Brazil        |
| Brazil        | Costa Rica    | 1 - 0   | 91% Brazil        |
| Brazil        | Serbia        | 1 - 0   | 89% Brazil        |
| Switzerland   | Costa Rica    | 0 - 1   | 69% Switzerland   |
| Switzerland   | Serbia        | 1 - 2   | 66% Switzerland   |
| Costa Rica    | Serbia        | 0 - 0   | 54% Serbia        |
+---------------+---------------+---------+-------------------+


+---------------+
| Group F       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| Germany       | Mexico        | 4 - 1   | 79% Germany       |
| Germany       | Sweden        | 5 - 3   | 84% Germany       |
| Germany       | South Korea   | 0 - 0   | 88% Germany       |
| Mexico        | Sweden        | 0 - 1   | 58% Mexico        |
| Mexico        | South Korea   | 0 - 0   | 67% Mexico        |
| Sweden        | South Korea   | 0 - 0   | 59% Sweden        |
+---------------+---------------+---------+-------------------+


+---------------+
| Group G       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| Belgium       | Panama        | 0 - 0   | 83% Belgium       |
| Belgium       | Tunisia       | 1 - 0   | 83% Belgium       |
| Belgium       | England       | 0 - 1   | 52% England       |
| Panama        | Tunisia       | 0 - 0   | 50% Panama        |
| Panama        | England       | 0 - 0   | 84% England       |
| Tunisia       | England       | 0 - 2   | 84% England       |
+---------------+---------------+---------+-------------------+


+---------------+
| Group H       |
+---------------+---------------+---------+-------------------+
| Team 1        | Team 2        | Score   | Elo Win Expect.   |
|---------------+---------------+---------+-------------------|
| Poland        | Senegal       | 0 - 0   | 63% Poland        |
| Poland        | Colombia      | 1 - 2   | 64% Colombia      |
| Poland        | Japan         | 0 - 2   | 72% Poland        |
| Senegal       | Colombia      | 2 - 2   | 75% Colombia      |
| Senegal       | Japan         | 1 - 0   | 60% Senegal       |
| Colombia      | Japan         | 4 - 1   | 82% Colombia      |
+---------------+---------------+---------+-------------------+
```
