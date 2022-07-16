import datetime

class player:
    def __init__(self,fname,lname,birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year

    def get_age(self):
        # now = datetime.datetime.now()
        return (datetime.datetime.now().year-self.birth_year)

    
class CricketPlayer(player):
    def __init__(self, fname, lname, birth_year, team):
        player.__init__(self,fname, lname, birth_year)
        self.team = team
        self.score = []

    def add_score(self, score):
        self.score.append(score)
    
    def get_average_score(self):
        return sum(self.score)/len(self.score)

    
class TennisPlayer(player):
    def __init__(self,fname, lname, birth_year, gwinner, team=''):
        player.__init__(self, fname, lname, birth_year)
        self.gwinner = gwinner
        self.team = team
        self.aces = []
    
    def get_average_aces_per_match(self):
        return sum(self.aces)/len(self.aces)
    

virat = CricketPlayer("virat", "kohli", 1988, "india")

roger = TennisPlayer("Roger","federer",1986,20,"Unknown")

print(virat.get_age())
print(roger.team)