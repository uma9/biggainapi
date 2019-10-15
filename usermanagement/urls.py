from django.urls import path,include,re_path
from .views import ValidatePhoneSendOTP
from .views import ValidateOTP,Register


app_name='usermanagement'
urlpatterns = [
    re_path(r'^validate_phone/',ValidatePhoneSendOTP.as_view()),
    re_path(r'^validate_otp/$',ValidateOTP.as_view()),
    re_path(r'^register/$',Register.as_view()),
]