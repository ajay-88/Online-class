from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def func1(request):
    return render(request,'index.html')

def Python(request):
    return render(request,'Python.html')

def MernStack(request):
    return render(request,'MernStack.html')

def DataScience(request):
    return render(request,'DataScience.html')

def DigitalMarketing(request):
    return render(request,'DigitalMarketing.html')

def Flutter(request):
    return render(request,'Flutter.html')

def PythonRegister(request):
    return render(request,'Python-register.html')

def PythonBookNow(request):
    return render(request,'Python-booknow.html')

def MernStackRegister(request):
    return render(request,'MernStack-register.html')

def MernStackBookNow(request):
    return render(request,'MernStack-booknow.html')

def DataScienceRegister(request):
    return render(request,'DataScience-register.html')

def DataScienceBookNow(request):
    return render(request,'DataScience-booknow.html')

def DigitalMarketingRegister(request):
    return render(request,'DigitalMarketing-register.html')

def DigitalMarketingBookNow(request):
    return render(request,'DigitalMarketing-booknow.html')

def FlutterRegister(request):
    return render(request,'Flutter-register.html')

def FlutterBookNow(request):
    return render(request,'Flutter-booknow.html')






def Python_register(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        qualification=request.POST['qualification']
        address = request.POST['address']

        data=register.objects.create(full_name=name,phone=phone,email=email,photo=photo,qualification=qualification,address=address)
        data.save()
        return render(request,'Python.html')

def MernStack_register(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        qualification=request.POST['qualification']
        address = request.POST['address']

        data=register.objects.create(full_name=name,phone=phone,email=email,photo=photo,qualification=qualification,address=address)
        data.save()
        return render(request,'MernStack.html')

def DataScience_register(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        qualification=request.POST['qualification']
        address = request.POST['address']

        data=register.objects.create(full_name=name,phone=phone,email=email,photo=photo,qualification=qualification,address=address)
        data.save()
        return render(request,'DataScience.html')


def DigitalMarketing_register(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        qualification=request.POST['qualification']
        address = request.POST['address']

        data=register.objects.create(full_name=name,phone=phone,email=email,photo=photo,qualification=qualification,address=address)
        data.save()
        return render(request,'DigitalMarketing.html')

def Flutter_register(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        qualification=request.POST['qualification']
        address = request.POST['address']

        data=register.objects.create(full_name=name,phone=phone,email=email,photo=photo,qualification=qualification,address=address)
        data.save()
        return render(request,'Flutter.html')



def Python_booking(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'Python.html')


def MernStack_booking(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'MernStack.html')


def DataScience_booking(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'DataScience.html')

def DigitalMarketing_booking(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'DigitalMarketing.html')


def Flutter_booking(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'Flutter.html')


def UserHomePage(request):
    return render(request,'User-Homepage.html')

def UserLogin(request):
    return render(request,'User-login.html')

def UserSignUp(request):
    return render(request,'User-signup.html')

def User_SignUp(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']

        data=userlogs.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password)
        data.save()
        return render(request,'User-login.html')

def User_login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        data=userlogs.objects.filter(email=email)
        if data:
            data1=userlogs.objects.get(email=email)
            if data1.password==password:
                request.session['id']=email
                return render(request,'User-Homepage.html')
            else:
                messages.info(request,'invalid E-mail or password')
                return redirect(UserLogin)
        else:
            messages.info(request,'invalid E-mail or password')
            return redirect(UserLogin)

def AdminLoginPage(request):
    return render(request,'Admin-login.html')

def AdminHomePage(request):
    return render(request,'Admin-Homepage.html')

def Admin_login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        data=admin_log.objects.filter(admin_name=name)
        if data:
            data1=admin_log.objects.get(admin_name=name)
            if data1.admin_pass==password:
                request.session['id']=name
                return render(request,'Admin-Homepage.html')
            else:
                messages.info(request,'invalid E-mail or password')
                return redirect(AdminLoginPage)
        else:
            messages.info(request,'invalid E-mail or password')
            return redirect(AdminLoginPage)

def TutorLogin(request):
    return render(request,'Tutor-Login.html')

def TutorSignup(request):
    return render(request,'Tutor-signup.html')

def Tutor_SignUp(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        qualification = request.POST['qualification']
        email=request.POST['email']
        password=request.POST['password']

        data=tutorlogs.objects.create(full_name=name,phone=phone,email=email,qualification=qualification,photo=photo,password=password)
        data.save()
        return render(request,'Tutor-Login.html')

# def AdminTutorVerification(request):
#     return render(request,'Admin-tutorverification.html')

def AdminTutorVerification(request):
    d=tutorlogs.objects.filter(status="pending")
    return render(request,'Admin-tutorverification.html',{'data':d})

def Admin_deleteTutor(request,id):
    tutorlogs.objects.filter(pk=id).delete()
    return redirect(AdminTutorVerification)

def Admin_acceptTutor(request,id):
    tutorlogs.objects.filter(pk=id).update(status='approve')
    return redirect(AdminTutorVerification)

def Tutor_login(request):
    if request.method=='POST':
        gmail=request.POST['email']
        password=request.POST['password']
        data=tutorlogs.objects.filter(email=gmail)
        if data:
            data1=tutorlogs.objects.get(email=gmail)
            if data1.password==password:
                request.session['id']=gmail
                if data1.status=="approve":
                    return render(request, 'Tutor-Homepage.html')
                else:
                    messages.info(request, 'invalid E-mail or password')
                    return redirect(TutorLogin)
            else:
                messages.info(request,'invalid E-mail or password')
                return redirect(TutorLogin)
        else:
            messages.info(request,'invalid E-mail or password')
            return redirect(TutorLogin)

def Usercertificateupload(request):
    return render(request,'User-certificateUpload.html')

def Userplacement(request):
    return render(request,'User-Placement.html')

def User_Certificate_Upload(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        certi10 = request.FILES['certi10']
        certi12 = request.FILES['certi12']
        degree = request.FILES['degree']


        data=usercertificates.objects.create(full_name=name,email=email,certi10=certi10,certi12=certi12,degree=degree)
        data.save()
        return render(request,'User-certificateUpload.html')


def videocall(request):
    return render(request,'VideoCall.html')


def CompanyA(request):
    return render(request,'User-CompanyA.html')

def User_CompanyA(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']


        data=userplacement.objects.create(full_name=name,email=email,resume=resume)
        data.save()
        return render(request,'User-Placement.html')

def CompanyB(request):
    return render(request,'User-CompanyB.html')

def User_CompanyB(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']


        data=userplacement.objects.create(full_name=name,email=email,resume=resume)
        data.save()
        return render(request,'User-Placement.html')

def CompanyC(request):
    return render(request,'User-CompanyC.html')

def User_CompanyC(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']


        data=userplacement.objects.create(full_name=name,email=email,resume=resume)
        data.save()
        return render(request,'User-Placement.html')


def Pythontrail(request):
    return render(request,'Python-trail.html')

def Python_Trail(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'Python.html')

def Mernstacktrail(request):
    return render(request,'MernStack-trail.html')

def MernStack_Trail(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'MernStack.html')

def Datasciencetrail(request):
    return render(request,'DataScience-trail.html')

def DataScience_Trail(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'DataScience.html')

def Digitalmarketingtrail(request):
    return render(request,'DigitalMarketing-trail.html')

def DigitalMarketing_Trail(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'DigitalMarketing.html')

def Fluttertrail(request):
    return render(request,'Flutter-trail.html')

def Flutter_Trail(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        photo = request.FILES['photo']
        email=request.POST['email']
        password=request.POST['password']
        payment_id=request.POST['payid']

        data=booking.objects.create(full_name=name,phone=phone,email=email,photo=photo,password=password,payment_id=payment_id)
        data.save()
        return render(request,'Flutter.html')






