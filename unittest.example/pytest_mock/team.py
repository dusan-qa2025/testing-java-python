class Team():
    name = ''
    won = 0
    lost = 0
    position = 0

    def __init__(self, name, won, lost, position):
        self.name = name
        self.won = won
        self.lost = lost
        self.position = position

    def get_top_8():
        # Logic for reading top 8 teams from database
        print("Reading team from database...")
        