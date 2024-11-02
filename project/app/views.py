from django.shortcuts import render,redirect
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from .models import Otp
from datetime import datetime,timedelta


def home(req):
    return render(req,"home.html")


def emailotp(req):
    if req.method == 'POST':
        receiveremail = req.POST['email']
        a = random.randint(100000, 999999)  
        subject = 'your OTP  verification code'
        dattime = datetime.now()
        datetim = dattime + timedelta(minutes=0.5)  
        print(datetim)
        
        message = f'your OTP is {a}. please use this to verify '
        email_from = 'ramraja.e99@gmail.com'
        toemail = receiveremail
        send_mail(subject, message, email_from, [toemail])
        obj = Otp()
        obj.email = receiveremail
        obj.otp = a
        obj.otpexpriedtime = datetim
        obj.save()
        return render(req, "verify.html", {'email': receiveremail})
    else:
        return redirect("home")

def verifyotp(req):
    if req.method == "POST":
        email = req.POST['email']
        otp = req.POST['otp']
        email_record = Otp.objects.filter(email=email).last()
        if email_record:
            otpnum = int(email_record.otp)
            otps = int(otp)
            if otpnum == otps:
                from datetime import datetime
                expri = email_record.otpexpriedtime
                dt_object = datetime.strptime(expri, "%Y-%m-%d %H:%M:%S.%f")
                curr=datetime.now()
                if curr <= dt_object:
                    print("is success")
                    # messages.success(req,"your otp is correct")
                    # return render(req,'home.html')  
                    return HttpResponse('your otp is correct')
                else:
                    print('its expried')
                    # messages.error(req,"your otp is expried") 
                    # return render(req, 'home.html') 
                    return HttpResponse('your otp is expried') 
            else:
                return HttpResponse('OTP is incorrect') 
        else:
            return HttpResponse('OTP is incorrect') 
    else:
        return HttpResponse("OTP is incorrect")