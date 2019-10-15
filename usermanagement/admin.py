from django.contrib.auth import get_user_model
from django.contrib import admin
User=get_user_model()
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from .forms import UserAdminCreationForm,UserAdminChangeForm
from categories.models import Categories
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import PhoneOTP
admin.site.register(PhoneOTP)
admin.site.register(Categories)


# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    #form = UserAdminChangeForm
    #add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'phone','admin',)
    list_filter = ('staff','active','admin',)
    #'is_staff', 'is_active', 'is_admin',)
    #'is_admin', 'is_staff', 'is_active',
    fieldsets = (
        (None, {'fields': ('phone', 'password',)}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('admin','staff','active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2','user_id', 'name', 'email_id','active' ,'staff','admin' ,'is_advartiser','is_shopinguser','is_subscriber','is_vendor',)}
        ),
    )
    search_fields = ('phone','name',)
    ordering = ('phone','name',)
    filter_horizontal = ()

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin,self).get_inline_instances(request,obj)
# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)