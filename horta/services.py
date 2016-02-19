from queries import *


def startGrowing(user, plant):
    growingStage = getFirstGrowingStageByPlant(plant)
    return Growing.objects.create(user=user,stage=growingStage)


def getGrowning(user, plant):
    return getGrowingByUserAndPlant(user, plant)