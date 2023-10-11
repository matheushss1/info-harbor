import sys

import chess.pgn

from chess_results import download_all_pgns, parse_tournament_page
from player_finder import player_finder


def collect_tournament_data():

    tournament_id  = input("What is the Chess Results Tournament ID? ")
    return tournament_id


def tournament_scraper(tournament_id):
    players = parse_tournament_page(tournament_id)
    for player in players:
        player["color"] = "all"
        print(player)
        player_finder(player)


def main():

    if len(sys.argv) != 2:
        tournament_id = collect_tournament_data()
    else:
        tournament_id = sys.argv[1]

    tournament_scraper(tournament_id)


if __name__ == "__main__":
    main()
