from horta.models import *

def getFirstGrowingStageByPlant(plant):
    return GrowingStage.objects.get(plant=plant, step=1)

def getCurrentGrownStageByUserAndPlant(user, plant):
    return GrowingStage.objects.get(plant=plant, user=user)

def getUserByEmail(email):
    return User.objects.get(email=email)

def getGrowingByUserEmail(email):
    return Growing.objects.get(user__email=email)