from team import Team

def make_playoff_schedule():

    top_eight_teams = Team.get_top_8()
    pairs = []

    while len(top_eight_teams) > 0:
        pairs.append([top_eight_teams[0], top_eight_teams[-1]])
        top_eight_teams.pop(0)
        top_eight_teams.pop()

    return pairs
