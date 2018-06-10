#!/usr/bin/env python

from worldcup import WorldCup
from gamepredictor import HistoricalGamePredictor


if __name__ == "__main__":

    # Create World Cup 2018 object from groups file
    wc_2018 = WorldCup("groups.csv")

    # Create game predictor based on historical results
    hist_gp = HistoricalGamePredictor("results.csv")

    # Run predictions for the group stage
    wc_2018.play(hist_gp)

    # Print all game predictions
    wc_2018.print_game_results()
