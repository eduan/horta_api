from models import Growing
from queries import getFirstGrowingStageByPlant, getCurrentGrownStageByUserAndPlant

def startGrowing(user, plant):
    growingStage = getFirstGrowingStageByPlant(plant)
    return Growing.objects.create(user=user,stage=growingStage)

def getCurrentGrownStage(user, plant):
    return getCurrentGrownStageByUserAndPlant(user, plant)