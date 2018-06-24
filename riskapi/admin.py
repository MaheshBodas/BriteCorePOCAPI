from django.contrib.auth.models import User
from django.contrib import admin

from .models import (
    User,
    risktype,
    risk
)

# admin.site.register(User)
admin.site.register(risktype)
admin.site.register(risk)
