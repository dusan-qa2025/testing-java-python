def get_top_8_stub():
    return [
        ["Olympiacos Piraeus", 24, 10, 1],
        ["FC Barcelona", 23, 11, 2],
        ["Real Madrid", 23, 11, 3],
        ["AS Monako", 22, 12, 4],
        ["Maccabi Tel Aviv", 20, 14, 5],
        ["Partizan Belgrade", 20, 14, 6],
        ["Zalgiris Kaunas", 19, 15, 7],
        ["Fenerbahce Istanbul", 19, 15, 8],    
        ]




def make_playoff_schedule():
    result = make_playoff_schedule(get_top_8_stub());
    # compare expected and actual result
