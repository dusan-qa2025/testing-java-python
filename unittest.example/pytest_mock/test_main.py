from team import Team
from main import make_playoff_schedule

def test_make_playoff_schedule(mocker):

    def top_8_data():
        teams = [
            Team("Olympiacos Piraeus", 24, 10, 1),
            Team("KK Barcelona", 23, 11, 2),
            Team("Real Madrid", 23, 11, 3),
            Team("AS Monaco", 22, 12, 4),
            Team("Maccabi Tel Aviv", 20, 14, 5),
            Team("Partizan Belgrade", 20, 14, 6),
            Team("Zalgiris Kaunas", 19, 15, 7),
            Team("Fenerbahce Istanbul", 19, 15, 8)
        ]
        return teams
    
    mocker.patch( 'team.Team.get_top_8', top_8_data)

    result = make_playoff_schedule()

    assert result[0][0].position == 1
    assert result[0][1].position == 8
    assert result[2][1].name == "Partizan Belgrade"
    