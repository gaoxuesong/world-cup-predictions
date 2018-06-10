# world-cup-predictions
Predict the results of FIFA World Cup 2018 group stage using historical game results.

## Approach

In current version, a super simplistic approach is used: for a given game, if the two teams met before, the score of the most recent game is predicted. If the teams never met, a 0-0 raw is predicted.

## Dataset

The [results.csv](./results.csv) file comes from the [International football results from 1872 to 2018 Kaggle dataset](https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017), courtesy of [Mart Jürisoo](https://www.kaggle.com/martj42).

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
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| Russia        | Saudi Arabia  | 2 - 4   |
| Russia        | Egypt         | 0 - 0   |
| Russia        | Uruguay       | 1 - 1   |
| Saudi Arabia  | Egypt         | 0 - 1   |
| Saudi Arabia  | Uruguay       | 1 - 1   |
| Egypt         | Uruguay       | 0 - 2   |
+---------------+---------------+---------+


+---------------+
| Group B       |
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| Portugal      | Spain         | 0 - 0   |
| Portugal      | Morocco       | 1 - 3   |
| Portugal      | Iran          | 2 - 0   |
| Spain         | Morocco       | 3 - 2   |
| Spain         | Iran          | 0 - 0   |
| Morocco       | Iran          | 1 - 1   |
+---------------+---------------+---------+


+---------------+
| Group C       |
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| France        | Australia     | 6 - 0   |
| France        | Peru          | 0 - 1   |
| France        | Denmark       | 2 - 1   |
| Australia     | Peru          | 0 - 0   |
| Australia     | Denmark       | 0 - 2   |
| Peru          | Denmark       | 0 - 0   |
+---------------+---------------+---------+


+---------------+
| Group D       |
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| Argentina     | Iceland       | 0 - 0   |
| Argentina     | Croatia       | 2 - 1   |
| Argentina     | Nigeria       | 2 - 4   |
| Iceland       | Croatia       | 1 - 0   |
| Iceland       | Nigeria       | 3 - 0   |
| Croatia       | Nigeria       | 0 - 0   |
+---------------+---------------+---------+


+---------------+
| Group E       |
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| Brazil        | Switzerland   | 0 - 1   |
| Brazil        | Costa Rica    | 1 - 0   |
| Brazil        | Serbia        | 1 - 0   |
| Switzerland   | Costa Rica    | 0 - 1   |
| Switzerland   | Serbia        | 1 - 2   |
| Costa Rica    | Serbia        | 0 - 0   |
+---------------+---------------+---------+


+---------------+
| Group F       |
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| Germany       | Mexico        | 4 - 1   |
| Germany       | Sweden        | 5 - 3   |
| Germany       | South Korea   | 0 - 0   |
| Mexico        | Sweden        | 0 - 1   |
| Mexico        | South Korea   | 0 - 0   |
| Sweden        | South Korea   | 0 - 0   |
+---------------+---------------+---------+


+---------------+
| Group G       |
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| Belgium       | Panama        | 0 - 0   |
| Belgium       | Tunisia       | 1 - 0   |
| Belgium       | England       | 0 - 1   |
| Panama        | Tunisia       | 0 - 0   |
| Panama        | England       | 0 - 0   |
| Tunisia       | England       | 0 - 2   |
+---------------+---------------+---------+


+---------------+
| Group H       |
+---------------+---------------+---------+
| Team 1        | Team 2        | Score   |
|---------------+---------------+---------|
| Poland        | Senegal       | 0 - 0   |
| Poland        | Colombia      | 1 - 2   |
| Poland        | Japan         | 0 - 2   |
| Senegal       | Colombia      | 2 - 2   |
| Senegal       | Japan         | 1 - 0   |
| Colombia      | Japan         | 4 - 1   |
+---------------+---------------+---------+
```
