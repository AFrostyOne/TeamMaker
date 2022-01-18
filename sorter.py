from random import shuffle, choice
from sort import get_skill, show_players, add_player, assign_teams, assign_new_teams, get_team_skills, show_teams, get_remixes
from statistics import pvariance


players = {}


print("Hello, I am here to help you assign teams.")
print("How many teams are there going to be?")
while True:
    try:
        number_of_teams = int(input("> "))
    except ValueError:
        print("Number of teams must be an integer. Enter number of teams.")
        continue
    if number_of_teams > 10 or number_of_teams < 2:
        print("The minimum is 2. The maximum number of teams is 10.")
    else:
        break
print("How many times would you like team remixing?")
print("The more times, the fairer the teams will be. But, they will also be less random.")
remixes = get_remixes(0, 50)
print("Enter the first player")
player = add_player(players)
print(f"Enter a skill level for {player} from 1-10.")
players[player] = get_skill()
show_players(players)


for i in range(25):
    print("Enter the next player.")
    player = add_player(players)
    print(f"Enter the skill level for {player}")
    players[player] = get_skill()
    print("If there are no more players type 'done'. Otherwise type enter")
    response = input(">")
    if response == "done":
        break


show_players(players)

teams = assign_teams(players, number_of_teams)
for i in range(remixes):
    teams2 = assign_new_teams(teams)
    team_skills = get_team_skills(teams)
    team2_skills = get_team_skills(teams2)
    if pvariance(team2_skills) < pvariance(team_skills):
        teams = teams2



show_teams(teams)


"""
Ideas for next steps:
-clean up and make shorter
-Specify if certain players should (not) be on same team
"""