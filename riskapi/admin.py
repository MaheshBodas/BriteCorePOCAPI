from django.contrib import admin

from .models import (
    user,
    risktype,
    risk
)

admin.site.register(user)
admin.site.register(risktype)
admin.site.register(risk)
