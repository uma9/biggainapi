from django.shortcuts import render
from rest_framework.views import  APIView
from .models import User,PhoneOTP
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import random
from .serializer import  CreateUserSerializer
from rest_framework import viewsets
from usermanagement.serializer  import CreateUserSerializer


# Create your views here.
#link=f'https://2factor.in/API/R1/?module=PROMO_SMS&apikey=f87f18bc-d452-11e9-ade6-0200cd936042&to={phone}&from=biggai&msg=SMS_TEXT&var1={name}&var2={otpkey}'
#request.get(link)
class ValidatePhoneSendOTP(APIView):
    def post(self,request, *args, **kwargs):
        phone_number=request.data.get('phone')
        if phone_number:
            phone=str(phone_number)
            user=User.objects.filter(phone__iexact=phone)
            if user.exists():
                return Response({
                    'status':False,
                    'detail':'phonenumber allrady exits '
                })
            else:
                key= send_otp(phone)
                if key:
                    old=PhoneOTP.objects.filter(phone__iexact=phone)
                    if old.exists():
                        old=old.first()
                        count=old.count
                        if count>10:
                            return Response({
                                'status':False,
                                'details':'Sending otp error limmit exeed'
                                    })
                        old.count=count+1
                        old.save()

                        print("count increased", count)
                        return Response({
                            'status': True,
                            'details': 'OTP sent succusfully'
                        })


                    PhoneOTP.objects.create(
                       phone=phone,
                       otp=key,
                      )
                    return Response({
                       'status':True,
                       'details':'OTP sent succusfully'
                   })
                else:
                    return Response({
                        'status':False,
                        'detail':'sending otp error'
                    })
        else:
            return Response({
                'status':False,
                'details':'phone number is not given in post request'
            })
def send_otp(phone):
        if phone:
            key=random.randint(999,9999)
            print(key)
            return  key
        else:
            return False
class ValidateOTP(APIView):
    # if we have recived otp post a request with phone and that otp and you will be redirectd through set the password
   def post(self,request ,*args, **kwargs):
       phone=request.data.get('phone',False)
       otp_sent=request.data.get('otp',False)
       if phone and otp_sent:
           old=PhoneOTP.objects.filter(phone__iexact=phone)
           print(old)
           print('u')
           if old.exists():
               old=old.first()
               print(old)
               print('m')
               otp=old.otp
               print(otp)
               print('a')
               print(otp_sent)
               if str(otp_sent)==str(otp):
                   old.validated=True
                   old.save()
                   return Response({
                       'status':False,
                       'detail':'OTP Matched please proceed for registration'
                   })
               else:
                   return Response({
                       'status':False,
                       'detail':'OTP IN CORRECT'

                   })
           else:
               return Response({
                   'status':False,
                   'detail':'First proceed via sending otp request'
               })
       else:
           return Response({
               'detail':'please provide both phone and otp for validation'
           })

class Register(APIView):
    def post(self,request, *args,**kwargs):
        phone=request.data.get('phone',False)
        password= request.data.get('password',False)
        name=request.data.get('name',False)
        if phone and password:
            old=PhoneOTP.objects.filter(phone__iexact=phone)
            if old.exists():
                old=old.first()
                validated=old.validated
                if validated:
                    temp_data={
                        'phone':phone,
                        'password':password,
                        'name':name
                    }
                    serializer= CreateUserSerializer(data=temp_data)
                    serializer.is_valid(raise_exception=True)
                    User=serializer.save()
                    old.delete()
                    return Response({
                        'status':True,
                        'detail':'account create'
                    })
                else:
                     return Response({
                         'status':False,
                         'detail':'otp have not varified '
                     })
            else:
                return Response({
                    'status':False,
                    'detail':'please verify phone first'
                })
        else:
            return Response({
                'status':False,
                'detail':'Both phone and password are not set'
            })
