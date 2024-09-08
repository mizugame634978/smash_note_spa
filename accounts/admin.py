from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class UserAdmin(BaseUserAdmin):#管理画面でaccountsにたいして見た目を変える
    list_display = (#一覧表示の画面で出る項目
        "email",
        "active",
        "staff",
        "admin",
    )
    list_filter = (
        "admin",
        "active",
    )
    ordering = ("email",)
    filter_horizontal = ()

    search_fields=('email',)#ユーザー名ではなく、メアドで検索

    add_fieldsets = (#ユーザー登録画面に飛ぶためにいる
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    fieldsets = (#ユーザー編集ページに飛ぶためにいる
        (None, {'fields': ('email', 'password')}),
        ('権限', {'fields': ('staff','admin',)}),
    )

admin.site.register(User,UserAdmin)