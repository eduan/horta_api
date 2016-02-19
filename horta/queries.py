from horta.models import Growing, GrowingStage, User


def getFirstGrowingStageByPlant(plant):
    return GrowingStage.objects.get(plant=plant, step=1)


def getGrowingByUserAndPlant(user, plant):
    return Growing.objects.get(user=user)


def getGrowingByUserEmail(email):
    return Growing.objects.get(user__email=email)


def getUserByEmail(email):
    return User.objects.get(email=email)
