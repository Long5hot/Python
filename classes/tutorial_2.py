import datetime

class CricketPlayer :
    def __init__(self,fname,lname,team,birth_year) :
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def getAge(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_score(self,score):
        self.scores.append(score)

    def getAverage(self):
        return sum(self.scores)/len(self.scores)

    def __lt__(self,other):
        # other_score = other.getAverage()
        # return self.getAverage() < other.getAverage()
        pass
        
    # def __getattribute__(self, __name: str) -> Any:
        # pass
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

virat = CricketPlayer("virat","Kohli","India",1988)
david = CricketPlayer("David","Warner","Aus",1980)

virat.add_score(100)
virat.add_score(1)

virat_average = virat.getAverage()

print(virat.first_name)


print("Average of virat  " + str(virat_average))

print(virat<david)


print(virat)