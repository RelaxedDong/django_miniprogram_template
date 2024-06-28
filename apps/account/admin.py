from django.contrib import admin

from apps.account.models import AccountModel


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'gender', 'openid', 'wechat', 'created_time', 'last_login']
    search_fields = ['nickname', 'openid']
    model_icon = 'fa fa-user-o'
    ordering = ["-last_login"]


admin.site.register(AccountModel, AccountAdmin)
