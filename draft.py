import time
from Player import *
from Team import *
from PlayerList import *
from DraftOrder import *


for team in order:
    print("With the #{} of the MLB draft the {} pick".format(team.draftPosition, team.name))
    time.sleep(1.5)
    print("{} from {} a {}".format(McClanahanSh.name, McClanahanSh.school, McClanahanSh.position))

for player in playerPool:
    print(player.name, player.position)