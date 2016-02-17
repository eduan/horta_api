from django.contrib import admin
from .models import Plant, Condition, ConditionType, ConditionInterval

admin.site.register(Plant)
admin.site.register(Condition)
admin.site.register(ConditionType)
admin.site.register(ConditionInterval)