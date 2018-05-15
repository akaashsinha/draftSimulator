RHP = "RHP"
LHP = "LHP"
catcher = "Catcher"
first_base = "1B"
second_base = "2B"
third_base = "3B"
SS = "SS"
LF = "LF"
CF = "CF"
RF = "RF"

positions = [RHP, catcher, first_base, second_base, third_base, SS, LF, CF, RF, LHP]


class Player(object):
    name = ""
    position = 0
    school = ""
    ranking = 0
    cost = 0

    def __init__(self, name, position, school, ranking, cost=0):
        self.name = name
        self.position = positions[position]
        self.school = school
        self.ranking = ranking
        self.cost = cost

    def __repr__(self):
        return repr((self.name, self.position, self.school, self.ranking, self.cost))
