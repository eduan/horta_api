from horta.models import GrowingStage

def getFirstGrowingStageByPlant(plant):
    return GrowingStage.objects.get(plant=plant, step=1)

def getCurrentGrownStageByUserAndPlant(user, plant):
    return GrowingStage.objects.get(plant=plant, user=user)
