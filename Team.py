class Team(object):
    name = ""
    draftPosition = 0

    def __init__(self, name, draftPosition, bonusPool):
        self.name = name
        self.draftPosition = draftPosition
        self.School = ""
        self.bonusPool = bonusPool

    def __repr__(self):
        return repr((self.name, self.draftPosition, self.bonusPool))

tigers = Team("Detroit Tigers", 1, 8096300)
giants = Team("San Francisco Giants", 2, 7494600)
