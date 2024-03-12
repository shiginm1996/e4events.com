from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.core.mail import send_mail
from eventpro.settings import EMAIL_HOST_USER

# Create your views here.

def sample(self):
    return HttpResponse('Hello World!')


def event_index(request):
    return render(request,'index.html')

def user_reg(request):
    if request.method=='POST':
        profile=request.FILES.get('profile')
        name=request.POST.get('first_name')
        address=request.POST.get('address')
        district=request.POST.get('district')
        usertype=request.POST.get('usertype')
        username=request.POST.get('user_name')
        password=request.POST.get('user_password')
        cpassword=request.POST.get('confirm_password')
        email=request.POST.get('email')
        website=request.POST.get('website')
        phone=request.POST.get('contact_no')
        if password==cpassword:
            a=register(profile=profile,name=name,address=address,district=district,usertype=usertype,username=username,password=password,email=email,website=website,phone=phone)
            a.save()
            subject = f'Registration Successfull....'
            message = 'Dear "%s",\n We are delighted to inform you that your registration with E4Event.com was successful! Welcome to our community.\n\n Best regards,\n  E4Event.com' % name

            email_from = EMAIL_HOST_USER
            sendmail = 'shiginmadappally5@gmail.com'
            send_mail(
                subject,
                message,
                email_from,
                [sendmail]
            )
            return redirect(user_login)
        # else:
        #     return HttpResponse('Registered Successfully')
    return render(request,'2.user_registration.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        a=register.objects.all()
        for i in a:
            if i.email==username and i.password==password and i.usertype=='company':
                request.session['id1']=i.id
                return redirect(event_company_page)
            elif i.email==username and i.password==password and i.usertype=='customer':
                request.session['id1']=i.id
                return redirect(customer_profile)
        else:
            return HttpResponse('Invalid Username or Password')
    return render(request,'1.loginpage.html')

def seller_user_display(request):
    idd=request.session['id1']
    bb=register.objects.get(id=idd)
    img=str(bb.profile).split('/')[-1]
    return render(request,'3.sellerdisplay.html',{'user':bb,'img':img})


def profile_edit(request,id):
    a=register.objects.get(id=id)
    img=str(a.profile).split('/')[-1]
    if request.method=='POST':
        if request.FILES.get('profile')==None:
            a.save()
        else:
            a.profile=request.FILES['profile']
            a.save()
        a.name=request.POST.get('first_name')
        a.address=request.POST.get('address')
        # if request.POST.get('district')==None:
        #     a.save()
        # else:
        #     a.district=request.POST.get('district')
        #     a.save()
        a.district = request.POST.get('district')
        a.username=request.POST.get('user_name')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('contact_no')
        a.save()
        subject = f'Profile Updation Successfull....'
        message = 'Dear "%s",\n Your profile updated Successfully. Please login our website for further updation\n\n Thank You\n  E4Event.com' %a.name

        email_from = EMAIL_HOST_USER
        sendmail = 'shiginmadappally5@gmail.com'
        send_mail(
            subject,
            message,
            email_from,
            [sendmail]
        )

        return redirect(seller_user_display)

    return render(request,'4.1.editpage1.html',{'user':a,'img':img})


def customer_edit(request, id):
    a = register.objects.get(id=id)
    img = str(a.profile).split('/')[-1]
    if request.method == 'POST':
        if request.FILES.get('profile') == None:
            a.save()
        else:
            a.profile = request.FILES['profile']
            a.save()
        a.name = request.POST.get('first_name')
        a.address = request.POST.get('address')
        # if request.POST.get('district')==None:
        #     a.save()
        # else:
        #     a.district=request.POST.get('district')
        #     a.save()
        a.district = request.POST.get('district')
        a.username = request.POST.get('user_name')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('contact_no')
        a.save()
        subject = f'Profile Updation Successfull....'
        message = 'Dear "%s",\n Your profile updated Successfully. Please login our website for further updation\n\n Thank You\n  E4Event.com' % a.name

        email_from = EMAIL_HOST_USER
        sendmail = 'shiginmadappally5@gmail.com'
        send_mail(
            subject,
            message,
            email_from,
            [sendmail]
        )

        return redirect(customer_dis)

    return render(request, '4.2.editpage2.html', {'user': a, 'img': img})


def logoutfun(request):
    logout(request)
    return redirect(user_login)


def customer_profile(request):
    id=[]
    profile=[]
    name=[]
    address=[]
    district=[]
    email=[]
    phone=[]
    usertype=[]
    idd1=request.session['id1']
    bb=register.objects.get(id=idd1)
    imgg=str(bb.profile).split('/')[-1]

    a=register.objects.all()

    for i in a:
        if i.usertype == 'company':
            id1=i.id
            id.append(id1)
            profile1=str(i.profile).split('/')[-1]
            profile.append(profile1)
            name1=i.name
            name.append(name1)
            address1=i.address
            address.append(address1)
            district1=i.district
            district.append(district1)
            email1=i.email
            email.append(email1)
            phone1=i.phone
            phone.append(phone1)
            usertype1=i.usertype
            usertype.append(usertype1)
    mylist=zip(id,profile,name,address,district,email,phone,usertype)
    return render(request,'5.eventteam.html',{'data':mylist,'user2':bb,'img2':imgg})


def eventbooking(request,id):
    user2=register.objects.get(id=id)
    idd=request.session['id1']
    user3=register.objects.get(id=idd)
    if request.method=='POST':
        fname=request.POST.get('first_name')
        event_type=request.POST.get('eventtype')
        event_team=request.POST.get('eventteam')
        email=request.POST.get('email')
        address = request.POST.get('address')
        event_date=request.POST.get('edate')
        phone=request.POST.get('phone')
        alt_phone = request.POST.get('aphone')
        amount=request.POST.get('amount')
        description=request.POST.get('description')
        b=eventbookmodel(first_name=fname,event_type=event_type,event_team=event_team,email=email,address=address,event_date=event_date,phone=phone,alternate_phone=alt_phone,amount=amount,description=description)
        b.save()
        subject = f'Booking Successfull....'
        message = 'Dear "%s",\n We are delighted to inform you that your booking with "%s" was successful! \n Thank You For Choosing Us\n\n Best regards,\n  E4Event.com' % (fname,event_team)

        email_from = EMAIL_HOST_USER
        sendmail = 'shiginmadappally5@gmail.com'
        send_mail(
            subject,
            message,
            email_from,
            [sendmail]
        )
        return redirect(customer_profile)
    return render(request, '6.eventbooking.html', {'a':user2,'b':user3})


def event_company_page(request):
    count=[]
    id=[]
    name=[]
    event_type=[]
    event_team=[]
    email=[]
    address=[]
    event_date=[]
    phone=[]
    alternate_phone=[]
    amount=[]
    description=[]
    idd3=request.session['id1']
    user4=register.objects.get(id=idd3)
    b=eventbookmodel.objects.all()
    # c=0
    # for i in b:
    #     i.id=i.id-7
    #     for j in range(i.id):
    #         if i.event_team==user4.name:
    #             c+=1
    #     count=c

    for i in b:
        if i.event_team==user4.name:
            id1=i.id
            id.append(id1)
            name1=i.first_name
            name.append(name1)
            event_type1=i.event_type
            event_type.append(event_type1)
            event_team1=i.event_team
            event_team.append(event_team1)
            email1=i.email
            email.append(email1)
            address1=i.address
            address.append(address1)
            event_date1=i.event_date
            event_date.append(event_date1)
            phone1=i.phone
            phone.append(phone1)
            alternate_phone1=i.alternate_phone
            alternate_phone.append(alternate_phone1)
            amount1=i.amount
            amount.append(amount1)
            description1=i.description
            description.append(description1)
            count.append((id1, name1, event_type1, event_team1, email1, address1, event_date1, phone1,alternate_phone1,amount1,description1))

    mylist=zip(id,name,event_type,event_team,email,address,event_date,phone,alternate_phone,amount,description)
    count1=[]
    id=[]
    name=[]
    event_type=[]
    email=[]
    address=[]
    event_date=[]
    phone=[]
    alternate_phone=[]
    amount=[]
    description=[]
    status=[]
    idd4=request.session['id1']
    user5=register.objects.get(id=idd4)
    b=confirm_booking_model.objects.all()
    # c1 = 0
    # for i in b:
    #     i.id=i.id-7
    #     for j in range(i.id):
    #         if i.event_team == user4.name and i.confirm_order=='accept':
    #             c1 += 1
    #     count1 = c1
    for i in b:
        if i.event_team == user5.name and i.confirm_order=='accept':

            id1=i.id
            id.append(id1)
            name1=i.customer_name
            name.append(name1)
            event_type1=i.event_type
            event_type.append(event_type1)
            email1=i.email
            email.append(email1)
            address1=i.address
            address.append(address1)
            event_date1=i.event_date
            event_date.append(event_date1)
            phone1=i.phone
            phone.append(phone1)
            alternate_phone1=i.altern_phone
            alternate_phone.append(alternate_phone1)
            amount1=i.exp_amount
            amount.append(amount1)
            description1=i.description
            description.append(description1)
            status1=i.confirm_order
            status.append(status1)
            count1.append((id1, name1, event_type1,email1, address1, event_date1, phone1,alternate_phone1,amount1,description1))
    mylist1=zip(id,name,event_type,email,address,event_date,phone,alternate_phone,amount,description,status)
    count2=[]
    id = []
    name = []
    event_type = []
    email = []
    address = []
    event_date = []
    phone = []
    alternate_phone = []
    amount = []
    description = []
    status = []
    idd5 = request.session['id1']
    user6 = register.objects.get(id=idd5)
    c = confirm_booking_model.objects.all()
    # c2 = 0
    # for i in c:
    #     for j in range(i.id):
    #         if i.event_team == user4.name and i.confirm_order == 'reject':
    #             c2 += 1
    #     count2 = c2
    for i in c:
        if i.event_team == user6.name and i.confirm_order == 'reject':
            id1 = i.id
            id.append(id1)
            name1 = i.customer_name
            name.append(name1)
            event_type1 = i.event_type
            event_type.append(event_type1)
            email1 = i.email
            email.append(email1)
            address1 = i.address
            address.append(address1)
            event_date1 = i.event_date
            event_date.append(event_date1)
            phone1 = i.phone
            phone.append(phone1)
            alternate_phone1 = i.altern_phone
            alternate_phone.append(alternate_phone1)
            amount1 = i.exp_amount
            amount.append(amount1)
            description1 = i.description
            description.append(description1)
            status1 = i.confirm_order
            status.append(status1)
            count2.append((id1, name1, event_type1, email1, address1, event_date1, phone1,alternate_phone1,amount1,description1))
    mylist2 = zip(id, name, event_type, email, address, event_date, phone, alternate_phone, amount, description, status)
    name=[]
    rating=[]
    review=[]
    img=[]
    idd6 = request.session['id1']
    user7 = register.objects.get(id=idd6)
    dd=reviewmodel.objects.all()
    ee=register.objects.all()
    for i in dd:
        if i.event_teams == user7.name:
            print(i.event_teams)
            print(user7.name)
            name1=i.cust_name
            name.append(name1)
            rating1=i.rating
            rating.append(rating1)
            review1=i.review
            review.append(review1)
            for j in ee:
                if j.name==name1:
                    img1=str(j.profile).split('/')[-1]
                    img.append(img1)


    mylist3=zip(name,rating,review,img)
    return render(request,'7.company_page.html',{'user3':mylist,'cc':idd3,'user1':user4,'user2':mylist1,'dd':idd3,'user5':user5,'user4':mylist2,'ee':idd3,'user6':user6,'count':count,'count1':count1,'count2':count2,'user7':mylist3})





# def booking_status(request,id):
#     a=eventbookmodel.objects.get(id=id)
#     idd3 = request.session['id1']
#     user5 = register.objects.get(id=idd3)
#     return render(request,'8.booking_status.html',{'user':a,'user5':user5})


def confirm_book(request,id):
    a=eventbookmodel.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('cname')
        etype=request.POST.get('etype')
        eteam=request.POST.get('event_team')
        email=request.POST.get('email')
        address=request.POST.get('address')
        dbooking=request.POST.get('dbooking')
        ebooking=request.POST.get('ebooking')
        ebooking1=datetime.strptime(ebooking, "%B %d, %Y")
        ebooking2 = ebooking1.strftime("%Y-%m-%d")
        phone=request.POST.get('phone')
        aphone=request.POST.get('aphone')
        amount=request.POST.get('amount')
        des=request.POST.get('des')
        corder=request.POST.get('corder')
        aa=confirm_booking_model(customer_name=name,event_type=etype,event_team=eteam,email=email,address=address,date_of_booking=dbooking,event_date=ebooking2,phone=phone,altern_phone=aphone,exp_amount=amount,description=des,confirm_order=corder)
        aa.save()
        if aa.confirm_order=='accept':
            subject = f'Booking Confirmed....'
            message = 'Dear "%s",\n We hereby inform you that your booking with "%s" was Confirmed!\n Please visit our website for further enquiry.\n\n Best regards,\n  E4Event.com' % (name,eteam)

            email_from = EMAIL_HOST_USER
            sendmail = 'shiginmadappally5@gmail.com'
            send_mail(
                subject,
                message,
                email_from,
                [sendmail]
            )
        elif aa.confirm_order == 'reject':
            subject = f'Booking Rejected....'
            message = 'Dear "%s",\n We hereby inform you that your booking with "%s" was Rejected!\n Please visit our website for further enquiry.\n\n Best regards,\n  E4Event.com' % (
            name, eteam)

            email_from = EMAIL_HOST_USER
            sendmail = 'shiginmadappally5@gmail.com'
            send_mail(
                subject,
                message,
                email_from,
                [sendmail]
            )
        return redirect(seller_user_display)
    return render(request,'8.booking_status.html',{'user':a})



def customer_dis(request):
    edate=[]
    address=[]
    event_team=[]
    # status=[]
    id=[]
    idd7=request.session['id1']
    a=register.objects.get(id=idd7)
    img=str(a.profile).split('/')[-1]
    b=eventbookmodel.objects.all()
    c=register.objects.all()
    for i in b:
        if a.name==i.first_name:
            edate1=i.event_date
            edate.append(edate1)
            address1=i.address
            address.append(address1)
            event_team1=i.event_team
            event_team.append(event_team1)
            # status1=i.confirm_order
            # status.append(status1)
            id1=i.id
            id.append(id1)
    mylist=zip(edate,address,event_team,id)
    if request.method=='POST':
        custname=request.POST.get('name')
        event_teams=request.POST.get('eteam')
        rating=request.POST.get('rating')
        review=request.POST.get('review')
        aa=reviewmodel(cust_name=custname,event_teams=event_teams,rating=rating,review=review)
        aa.save()
        return redirect(customer_dis)
    id=[]
    name = []
    rating = []
    review = []
    imgg = []
    idd7 = request.session['id1']
    user8 = register.objects.get(id=idd7)
    dd = reviewmodel.objects.all()
    ee = register.objects.all()
    for i in dd:
        if i.cust_name == user8.name:
            id1=i.id
            id.append(id1)
            name1 = i.event_teams
            name.append(name1)
            rating1 = i.rating
            rating.append(rating1)
            review1 = i.review
            review.append(review1)
            for j in ee:
                if j.name == name1:
                    img1 = str(j.profile).split('/')[-1]
                    imgg.append(img1)

    mylist4 = zip(name, rating, review, imgg,id)
    return render(request,'9.customer_profile.html',{'data':a,'img':img,'data1':mylist,'data2':c,'data3':mylist4,'idd7':idd7})


def review_edit(request,id):
    a=reviewmodel.objects.get(id=id)
    b=register.objects.all()
    if request.method=='POST':
        a.cust_name=request.POST.get('name')
        if request.POST.get('eteam')==None:
            a.save()
        else:
            a.event_teams=request.POST.get('eteam')
            a.save()
        if request.POST.get('rating')==None:
            a.save()
        else:
            a.rating=request.POST.get('rating')
            a.save()
        a.review=request.POST.get('review')
        a.save()
        return redirect(customer_dis)
    return render(request,'10.review_edit.html',{'data':a,'data2':b})


def delete_review(request,id):
    dd=reviewmodel.objects.get(id=id)
    dd.delete()
    return redirect(customer_dis)

def admin_reg(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        a=admin_model(user_name=uname,password=password)
        a.save()
        return redirect(admin_login)
    return render(request,'13.admin_reg.html')
def admin_login(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        b = admin_model.objects.all()
        for i in b:
            if i.user_name==uname and i.password==passw:
                return redirect(admin_page)
        else:
            return HttpResponse('Invalid username or password')
    return render(request,'11.admin_login.html')

def admin_page(request):
    count1=[]
    id=[]
    name=[]
    usertype=[]
    address=[]
    phone=[]
    email=[]
    aa=register.objects.all()
    for i in aa:
        id1=i.id
        id.append(id1)
        name1=i.name
        name.append(name1)
        usertype1=i.usertype
        usertype.append(usertype1)
        address1=i.address
        address.append(address1)
        phone1=i.phone
        phone.append(phone1)
        email1=i.email
        email.append(email1)
        count1.append((id1,name1,usertype1,address1,phone1,email1))
    mylist1=zip(id,name,usertype,address,phone,email)
    count2 = []
    id = []
    name = []
    etype = []
    eteam = []
    edate = []
    phone = []
    bb=eventbookmodel.objects.all()
    for i in bb:
        id1 = i.id
        id.append(id1)
        name1 = i.first_name
        name.append(name1)
        etype1 = i.event_type
        etype.append(etype1)
        eteam1 = i.event_team
        eteam.append(eteam1)
        edate1 = i.event_date
        edate.append(edate1)
        phone1 = i.phone
        phone.append(phone1)
        count2.append((id1, name1, etype1, eteam1, edate1, phone1))
    mylist2 = zip(id, name, etype, eteam, edate, phone)
    count3=[]
    id=[]
    name=[]
    etype=[]
    eteam=[]
    edate=[]
    phone=[]
    cc=confirm_booking_model.objects.all()
    for i in cc:
        if i.confirm_order=='reject':
            id1=i.id
            id.append(id1)
            name1=i.customer_name
            name.append(name1)
            etype1=i.event_type
            etype.append(etype1)
            eteam1 = i.event_team
            eteam.append(eteam1)
            edate1=i.event_date
            edate.append(edate1)
            phone1=i.phone
            phone.append(phone1)
            count3.append((id1,name1,etype1,eteam1,edate1,phone1))
    mylist=zip(id,name,etype,eteam,edate,phone)
    return render(request,'12.admin_page.html',{'reg':mylist1,'booked':mylist2,'status':mylist,'count1':count1,'count2':count2,'count3':count3})


def admin_logoutfun(request):
    logout(request)
    return redirect(admin_login)

def admin_user_prof(request,id):
    a=register.objects.get(id=id)
    img=str(a.profile).split('/')[-1]

    return render(request,'20.adminuserprof.html',{'user':a,'img1':img})


def gallery(request):
    return render(request,'14.gallery.html')

def contact(request):
    return render(request,'15.contact.html')


def about(request):
    return render(request,'16.about.html')


def gallery2(request):
    return render(request,'17.gallery2.html')





def payment(request,id):
    a=confirm_booking_model.objects.get(id=id)

    return render(request,'18.payment.html',{'user':a})




def successfun(request):
    return render(request,'19.successpage.html')