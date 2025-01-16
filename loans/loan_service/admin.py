from django.contrib import admin

from .models import UserInformation, UserTransactionInformation

admin.site.register(UserInformation)
admin.site.register(UserTransactionInformation)
