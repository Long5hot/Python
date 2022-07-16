import datetime

virat = {
    "first_name": "Virat",
    "last_name": "kohli",
    "birth_year": 1988,
    "Scores": []
}

virat["Scores"].append(80)
virat["Scores"].append(100)
virat["Scores"].append(0)

def getAge(player):
    pass

def getAverage_score(player) :
    print(player["Scores"])
    print("Average : " + str(sum(player["Scores"])/len(player["Scores"])))
    return sum(player["Scores"])/len(player["Scores"])

def getAge(player):
    now = datetime.datetime.now()
    return now.year-player['birth_year']

david = {
    "first_name" : "david",
    "last_name" : "Warner",
    "Scores" : [],
    "birth_year" : 1986
}

getAverage_score(virat)
getAge(david)
getAge(virat)
print(getAge(david))
print(getAge(virat))