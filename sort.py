from random import choice
from copy import deepcopy


def get_skill():
    while True:
        try:
            skill = int(input(">"))
            if not 1 <= skill <= 10:
                raise ValueError
            break
        except ValueError:
            print("The skill level must be an integer from 1-10.")
    return skill


def show_players(players):
    print("Here are the current players:")
    for k, v in players.items():
        print("Player:", k)
        print(f"{k} Skill Level:", v)


def add_player(players: list):
    while True:
        player = input("Player Name:")
        if player in players:
            print("Player already entered. Player names must be unique. Try again.")
            continue
        else:
            break
    return player


def get_team_skills(teams: list):
    team_skills = []
    for t in teams:
        team_skills.append(sum(t.values()))
    return team_skills


def assign_teams(players: dict, number_of_teams):
    team1 = {}
    team2 = {}
    team3 = {}
    team4 = {}
    team5 = {}
    team6 = {}
    team7 = {}
    team8 = {}
    team9 = {}
    team10 = {}
    teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10]
    teams = teams[:number_of_teams]

    while players:
        for t in teams:
            if players:
                players_keys = players.keys()
                player = choice(list(players_keys))
                t[player] = players[player]
                del players[player]
    return teams


def assign_new_teams(teams: list):
    switch_players = {}
    teams2 = deepcopy(teams)
    for t2 in teams2:
        t2_players = list(t2.keys())
        t2_switch_player = choice(t2_players)
        switch_players[t2_switch_player] = t2[t2_switch_player]
        del t2[t2_switch_player]

    for t2 in teams2:
        switch_players_keys = list(switch_players.keys())
        receive_player = choice(switch_players_keys)
        t2[receive_player] = switch_players[receive_player]
        del switch_players[receive_player]
    return teams2


def show_teams(teams):
    i = 0
    for t in teams:
        i += 1
        print(f"Team {i}:")
        for k, v in t.items():
            print(f"Player: {k}  -- Skill: {v}")


def get_remixes(mininum: int, maximum: int):
    print(f"Enter the number of reshuffles desired ({mininum}-{maximum})")
    while True:
        try:
            remixes = int(input(">"))
        except ValueError:
            print("Remixes must be an integer.")
            continue
        if 0 <= remixes <51:
            break
        else:
            print(f"remixes must be an integer {mininum}-{maximum}")
