from django.shortcuts import render, HttpResponseRedirect
from .models import *
from datetime import date as d, datetime as dt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

######## HOME ########

def login(request):
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        data = Login.objects.filter(
            email=email, password=password, status="approved")
        if data:
            data = Login.objects.get(
                email=email, password=password, status="approved")

            if data.userType == "admin" and data.status == "approved":
                msg = "Welcome to Admin Page"
                return HttpResponseRedirect("/admin_home?msg="+msg)

            elif data.userType == "worker" and data.status == "approved":
                workdata = WorkersReg.objects.get(email=email)
                uid = workdata.id
                request.session['uid'] = uid
                msg = "Welcome to Worker Page"
                return HttpResponseRedirect("/worker_home?msg="+msg)

            elif data.userType == "user" and data.status == "approved":
                usrdata = UserReg.objects.get(email=email)
                uid = usrdata.id
                request.session['uid'] = uid
                msg = "Welcome to User Page"
                return HttpResponseRedirect("/user_home?msg="+msg)
        else:
            msg = "Invalid username or password provided"
    return render(request, 'login.html', {"msg": msg})

def userregistration(request):
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        gender = request.POST.get("Gender")
        image = request.FILES["image"]
        if UserReg.objects.filter(email=email).exists() or Login.objects.filter(email=email).exists():
            msg = "Email Already Registered"
        else:
            abc = Login.objects.create(
                email=email, password=password, userType='user')
            abc.save()
            reg = UserReg.objects.create(name=name, email=email, address=address,
                                         phone=phone, password=password, usrid=abc, image=image, gender=gender)
            reg.save()
            msg = "Registration Successful"
            return HttpResponseRedirect("/login?msg="+msg)
    return render(request, 'userregistration.html', {"msg": msg})

def workerregistration(request):
    msg = ""
    msg = request.GET.get('msg')
    cat = Category.objects.all()
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        image = request.FILES["image"]
        gender = request.POST.get("Gender")
        experience = request.POST.get("Experience")
        location = request.POST.get("Location")
        category = request.POST.get("Category")
        wages = request.POST.get("Wages")
        if WorkersReg.objects.filter(email=email).exists() or Login.objects.filter(email=email).exists():
            msg = "Email Already Registered"
        else:
            abc = Login.objects.create(
                email=email, password=password, userType='worker')
            abc.save()
            reg = WorkersReg.objects.create(name=name, email=email, address=address,
                                            phone=phone, password=password, worid=abc, image=image, gender=gender, experience=experience, location=location, category=category, wages=wages)

            reg.save()
            msg = "Registration Successful"
            return HttpResponseRedirect("/login?msg="+msg)
    return render(request, 'workerregistration.html', {"msg": msg, "cat": cat})

######## // HOME ########
######## ADMIN ########

def admin_home(request):
    msg = ""
    msg = request.GET.get('msg')
    return render(request, 'admin/adminhome.html', {"msg": msg})

def addcategory(request):
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        category = request.POST.get("Category")
        image = request.FILES["image"]
        abc = Category.objects.create(
            category=category, image=image)
        abc.save()
        msg = "Added Successfully"
    return render(request, 'admin/addcategory.html', {"msg": msg})

def viewuser(request):
    msg = request.GET.get("msg")
    abc = UserReg.objects.filter(status="pending")
    efg = UserReg.objects.filter(status="approved")
    hij = UserReg.objects.filter(status="blocked")
    return render(request, 'admin/viewuser.html', {"abc": abc, "efg": efg, "hij": hij, "msg": msg})

def blockuser(request):
    id = request.GET.get("id")
    UserReg.objects.filter(usrid=id).update(status="blocked")
    Login.objects.filter(id=id).update(status="blocked")
    return HttpResponseRedirect("/viewuser?msg=User Blocked")

def unblockuser(request):
    id = request.GET.get("id")
    UserReg.objects.filter(usrid=id).update(status="approved")
    Login.objects.filter(id=id).update(status="approved")
    return HttpResponseRedirect("/viewuser?msg=User Unblocked")

def approveuser(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    print(id)
    abc = UserReg.objects.filter(usrid=id).update(status="approved")
    efg = Login.objects.filter(id=id).update(status="approved")
    msg = "Approved"
    return HttpResponseRedirect("/viewuser?msg="+msg)

def rejecteduser(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("ab")
    aab = Login.objects.filter(id=id).delete()
    efg = UserReg.objects.filter(usrid=id).delete()
    msg = "Rejected"
    return HttpResponseRedirect("/viewuser?msg="+msg)

def deleteuser(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    email = request.GET.get("cd")
    abb = UserReg.objects.filter(email=email).delete()
    abo = Login.objects.filter(email=email).delete()
    msg = "Deleted employee"
    return HttpResponseRedirect("/viewuser", {"msg": msg})

def viewworker(request):
    msg = request.GET.get("msg")
    abc = WorkersReg.objects.filter(status="pending")
    efg = WorkersReg.objects.filter(status="approved")
    hij = WorkersReg.objects.filter(status="blocked")
    return render(request, 'admin/viewworker.html', {"abc": abc, "efg": efg, "hij": hij, "msg": msg})

def approveworker(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    print(id)
    abc = WorkersReg.objects.filter(worid=id).update(status="approved")
    efg = Login.objects.filter(id=id).update(status="approved")
    msg = "Approved"
    return HttpResponseRedirect("/viewworker?msg="+msg)

def blockworker(request):
    id = request.GET.get("id")
    WorkersReg.objects.filter(worid=id).update(status="blocked")
    Login.objects.filter(id=id).update(status="blocked")
    return HttpResponseRedirect("/viewworker?msg=Worker Blocked")

def unblockworker(request):
    id = request.GET.get("id")
    WorkersReg.objects.filter(worid=id).update(status="approved")
    Login.objects.filter(id=id).update(status="approved")
    return HttpResponseRedirect("/viewworker?msg=Worker Unblocked")

def rejectedworker(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("ab")
    aab = Login.objects.filter(id=id).delete()
    efg = WorkersReg.objects.filter(worid=id).delete()
    msg = "Rejected"
    return HttpResponseRedirect("/viewworker?msg="+msg)

def deleteworker(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    email = request.GET.get("cd")
    abb = WorkersReg.objects.filter(email=email).delete()
    abo = Login.objects.filter(email=email).delete()
    msg = "Deleted employee"
    return HttpResponseRedirect("/viewworker", {"msg": msg})

def userfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    abc = Useraddfeedback.objects.all()
    return render(request, 'admin/userfeedback.html', {"msg": msg, "abc": abc})

def viewcategory(request):
    msg = ""
    msg = request.GET.get("msg")
    abc = Category.objects.all()
    return render(request, 'admin/viewcategory.html', {"abc": abc, "msg": msg})

def editcategory(request):
    msg = ""
    id = request.GET.get("id")
    data = Category.objects.get(id=id)
    if request.POST:
        category = request.POST.get("category")
        image = request.FILES.get("image")
        if image:
            Category.objects.filter(id=id).update(category=category, image=image)
        else:
            Category.objects.filter(id=id).update(category=category)
        msg = "Updated Successfully"
        return HttpResponseRedirect("/viewcategory?msg="+msg)
    return render(request, 'admin/editcategory.html', {"i": data})

def deletecategory(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    abb = Category.objects.filter(id=id).delete()
    msg = "Deleted"
    return HttpResponseRedirect("/viewcategory", {"msg": msg})

def workerfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    abc = Workeraddfeedback.objects.all()
    return render(request, 'admin/workerfeedback.html', {"msg": msg, "abc": abc})

######## // ADMIN ########
######## USER ########

def user_home(request):
    msg = ""
    msg = request.GET.get('msg')
    return render(request, 'user/userhome.html', {"msg": msg})

def userviewcategory(request):
    msg = request.GET.get('msg')
    abc = Category.objects.all()
    return render(request, 'user/userviewcategory.html', {"abc": abc, "msg": msg})

def bookingcategory(request):
    msg = request.GET.get('msg')
    type = request.GET.get("type")
    abc = WorkersReg.objects.filter(category=type,status="approved")
    return render(request, 'user/bookingcategory.html', {"abc": abc, "msg": msg})

def bookworker(request):
    msg = ""
    msg = request.GET.get('msg')
    id = request.GET.get("id")
    # print(id, " 3333333333333333333333333333333333")
    uid = request.session['uid']
    # print(uid, " 3333333333333333333333333333333333")
    # worid = request.session['worid']
    rr = d.today()
    today = rr.strftime("%Y-%m-%d")
    abc = WorkersReg.objects.filter(id=id)
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        category = request.POST.get("Category")
        location = request.POST.get("Location")
        startingdate = request.POST.get("Startdate")
        endingdate = request.POST.get("Enddate")
        wages = request.POST.get("Wages")

        sdate = dt.strptime(startingdate, "%Y-%m-%d")
        edate = dt.strptime(endingdate, "%Y-%m-%d")

        date_diff = edate-sdate
        print("date_diff", date_diff)

        totalWage = (int(date_diff.days) + 1) * (int(wages))

        efg = Booking.objects.create(name=name, email=email, phone=phone, category=category, location=location,
                                     startingdate=startingdate, endingdate=endingdate, wages=totalWage, usrid_id=uid, worid=id)
        efg.save()
        msg = "Booked Successfully"
        return HttpResponseRedirect("/userviewcategory?msg="+msg)
    return render(request, 'user/bookworker.html', {"msg": msg, "abc": abc, "today": today})

def userviewbooking(request):
    msg = request.GET.get('msg')
    uid = request.session['uid']
    abc = Booking.objects.filter(usrid=uid, status="notbooked")
    efg = Booking.objects.filter(usrid=uid, status="approved")
    return render(request, 'user/userviewbooking.html', {"abc": abc, "efg": efg})

def cancelbooking(request):
    msg = ""
    id = request.GET.get("id")
    efg = Booking.objects.filter(id=id).delete()
    msg = "Cancelled"
    return HttpResponseRedirect("/userviewcategory?msg="+msg)

def useraddfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    bid = request.GET.get("bid")
    uid = request.session['uid']
    
    if not bid:
        return HttpResponseRedirect("/userviewpayment?msg=Invalid booking reference")
    
    try:
        booking = Booking.objects.get(id=bid)
    except Booking.DoesNotExist:
        return HttpResponseRedirect("/userviewpayment?msg=Work not found")
        
    worker_id = booking.worid
    abc = WorkersReg.objects.filter(id=worker_id)
    
    # Check if user already left feedback for this specific booking
    existing = Useraddfeedback.objects.filter(usrid_id=uid, booking_id=bid).first()
    if existing:
        msg = "You have already submitted feedback for this work. You can edit it from the My Feedbacks page."
        return HttpResponseRedirect("/user_my_feedbacks?msg="+msg)
        
    if request.POST:
        name = request.POST.get("Name")
        category = request.POST.get("Category")
        feedback = request.POST.get("Feedback")
        efg = Useraddfeedback.objects.create(
            category=category, name=name, feedback=feedback, usrid_id=uid, worid=worker_id, booking_id=bid)
        efg.save()
        msg = "Feedback Added Successfully"
        return HttpResponseRedirect("/userviewfeedback?id="+str(worker_id)+"&msg="+msg)
    return render(request, 'user/useraddfeedback.html', {"msg": msg, "abc": abc})

def userviewfeedback(request):
    id = request.GET.get("id")
    msg = request.GET.get("msg")
    uid = request.session['uid']
    abc = Useraddfeedback.objects.filter(worid=id)
    my_feedback = Useraddfeedback.objects.filter(usrid_id=uid, worid=id).first()
    return render(request, 'user/userviewfeedback.html', {"abc": abc, "worker_id": id, "my_feedback": my_feedback, "msg": msg, "uid": uid})

def user_my_feedbacks(request):
    uid = request.session.get('uid')
    msg = request.GET.get('msg')
    feedbacks = Useraddfeedback.objects.filter(usrid_id=uid)
    return render(request, 'user/user_my_feedbacks.html', {'feedbacks': feedbacks, 'msg': msg})

def edituseraddfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    feedback_id = request.GET.get("id")
    uid = request.session['uid']
    fb = Useraddfeedback.objects.filter(id=feedback_id, usrid_id=uid).first()
    if not fb:
        return HttpResponseRedirect("/userviewcategory?msg=Feedback not found")
    if request.POST:
        fb.feedback = request.POST.get("Feedback", fb.feedback)
        fb.save()
        msg = "Feedback Updated Successfully"
        return HttpResponseRedirect("/userviewfeedback?id="+str(fb.worid)+"&msg="+msg)
    return render(request, 'user/edituseraddfeedback.html', {"fb": fb, "msg": msg})

def deleteuseraddfeedback(request):
    feedback_id = request.GET.get("id")
    worker_id = request.GET.get("worid")
    uid = request.session['uid']
    Useraddfeedback.objects.filter(id=feedback_id, usrid_id=uid).delete()
    msg = "Feedback Deleted"
    return HttpResponseRedirect("/userviewfeedback?id="+str(worker_id)+"&msg="+msg)

def addfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    uid = request.session['uid']
    if request.POST:
        feedback = request.POST.get("Feedback")
        efg = Addfeedback.objects.create(
            feedback=feedback, usrid_id=uid)
        efg.save()
        msg = " Feedback Added Successfully"
    return render(request, 'user/addfeedback.html', {"msg": msg})

def userprofile(request):
    msg = request.GET.get('msg')
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = UserReg.objects.filter(id=uid)
    return render(request, 'user/userprofile.html', {"abc": abc, "msg": msg})

def updateuser(request):
    msg = ""
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = UserReg.objects.filter(usrid=id)
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        gender = request.POST.get("Gender")
        # image = request.FILES["image"]

        updatedata = UserReg.objects.filter(usrid=id).update(
            name=name, email=email, phone=phone, password=password, address=address, gender=gender)
        print(updatedata)
        logdata = Login.objects.filter(id=id).update(
            email=email, password=password)
        print(logdata)
        msg = "updated Successfully"
        return HttpResponseRedirect("/userprofile?msg="+msg)
    return render(request, 'user/updateuser.html', {"msg": msg, "abc": abc})

def payment(request):
    msg = ""
    msg = request.GET.get('msg')
    id = request.GET.get('id')
    efg = Booking.objects.filter(id=id)
    if request.POST:
        # Calculate 10% of the wages
        booking = Booking.objects.get(id=id)
        wage_amount = float(booking.wages)
        commission = wage_amount * 0.10
        
        # Create Payment record
        payment = Payment.objects.create(booking=booking, amount=commission)
        payment.save()

        abc = Booking.objects.filter(id=id).update(status="paid")
        msg = "Payment Successful"
        return HttpResponseRedirect("/userviewbooking?msg="+msg)
    return render(request, 'user/payment.html', {"msg": msg, "efg": efg})

def admin_payments(request):
    msg = request.GET.get('msg')
    payments = Payment.objects.all()
    return render(request, 'admin/admin_payments.html', {"payments": payments, "msg": msg})

def userviewpayment(request):
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = Booking.objects.filter(usrid=uid, status="paid")
    today = d.today().strftime("%Y-%m-%d")
    return render(request, 'user/userviewpayment.html', {"abc": abc, "today": today})

######## // USER ########
######## WORKER ########

def worker_home(request):
    msg = ""
    msg = request.GET.get('msg')
    return render(request, 'worker/workerhome.html', {"msg": msg})

def workerviewbooking(request):
    msg = request.GET.get('msg')
    uid = request.session['uid']
    abc = Booking.objects.filter(worid=uid, status="notbooked")
    efg = Booking.objects.filter(worid=uid, status="approved")
    return render(request, 'worker/workerviewbooking.html', {"abc": abc, "msg": msg, "efg": efg})

def workerviewhistory(request):
    msg = request.GET.get('msg')
    uid = request.session['uid']
    abc = Booking.objects.filter(worid=uid, status="paid")
    today = d.today().strftime("%Y-%m-%d")
    return render(request, 'worker/workerviewhistory.html', {"abc": abc, "msg": msg, "today": today})

def approvebooking(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    print(id)
    efg = Booking.objects.filter(id=id).update(status="approved")
    msg = "Approved"
    return HttpResponseRedirect("/worker_home?msg="+msg)

def rejectbooking(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    efg = Booking.objects.filter(id=id).delete()
    msg = "Rejected"
    return HttpResponseRedirect("/worker_home?msg="+msg)

def deletebooking(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    abb = Booking.objects.filter(id=id).delete()
    msg = "Deleted"
    return HttpResponseRedirect("/worker_home?msg="+msg)

def workerviewfeedback(request):
    uid = request.session['uid']
    # Feedbacks received from users
    user_feedbacks = Useraddfeedback.objects.filter(worid=uid)
    # Feedbacks given by worker to users
    worker_feedbacks = Workeraddfeedback.objects.filter(worid_id=uid)
    return render(request, 'worker/workerviewfeedback.html', {
        "user_feedbacks": user_feedbacks, 
        "worker_feedbacks": worker_feedbacks
    })

def workeraddfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    bid = request.GET.get("bid")
    uid = request.session['uid']
    
    if not bid:
        return HttpResponseRedirect("/workerviewpayment?msg=Invalid booking reference")
        
    try:
        booking = Booking.objects.get(id=bid)
    except Booking.DoesNotExist:
        return HttpResponseRedirect("/workerviewpayment?msg=Work not found")
        
    user_id = booking.usrid_id
    
    # Check if worker already left feedback for this specific booking
    existing = Workeraddfeedback.objects.filter(worid_id=uid, booking_id=bid).first()
    if existing:
        msg = "You have already submitted feedback for this work."
        return HttpResponseRedirect("/workerviewpayment?msg="+msg)
        
    if request.POST:
        feedback = request.POST.get("Feedback")
        efg = Workeraddfeedback.objects.create(
            feedback=feedback, worid_id=uid, usrid_id=user_id, booking_id=bid)
        efg.save()
        msg = " Feedback Added Successfully"
        return HttpResponseRedirect("/workerviewpayment?msg="+msg)
    return render(request, 'worker/workeraddfeedback.html', {"msg": msg, "booking": booking})

def editworkeraddfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    feedback_id = request.GET.get("id")
    uid = request.session['uid']
    fb = Workeraddfeedback.objects.filter(id=feedback_id, worid_id=uid).first()
    if not fb:
        return HttpResponseRedirect("/workerviewfeedback?msg=Feedback not found")
    if request.POST:
        fb.feedback = request.POST.get("Feedback", fb.feedback)
        fb.save()
        msg = "Feedback Updated Successfully"
        return HttpResponseRedirect("/workerviewfeedback?msg="+msg)
    return render(request, 'worker/editworkeraddfeedback.html', {"fb": fb, "msg": msg})

def deleteworkeraddfeedback(request):
    feedback_id = request.GET.get("id")
    uid = request.session['uid']
    Workeraddfeedback.objects.filter(id=feedback_id, worid_id=uid).delete()
    msg = "Feedback Deleted"
    return HttpResponseRedirect("/workerviewfeedback?msg="+msg)

def workerprofile(request):
    msg = request.GET.get('msg')
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = WorkersReg.objects.filter(id=uid)
    return render(request, 'worker/workerprofile.html', {"abc": abc, "msg": msg})

def updateworker(request):
    msg = ""
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = WorkersReg.objects.filter(worid=id)
    cat = Category.objects.all()
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        image = request.FILES.get("image")
        gender = request.POST.get("Gender")
        experience = request.POST.get("Experience")
        location = request.POST.get("Location")
        category = request.POST.get("Category")
        wages = request.POST.get("Wages")
        
        worker = WorkersReg.objects.get(worid=id)
        worker.name = name
        worker.email = email
        worker.phone = phone
        worker.password = password
        worker.address = address
        worker.gender = gender
        worker.experience = experience
        worker.location = location
        worker.category = category
        worker.wages = wages
        if image:
            worker.image = image
        worker.save()

        logdata = Login.objects.filter(id=id).update(
            email=email, password=password)
        print(logdata)
        msg = "updated Successfully"
        return HttpResponseRedirect("/workerprofile?msg="+msg)
    return render(request, 'worker/updateworker.html', {"msg": msg, "abc": abc, "cat": cat})

def workerviewpayment(request):
    msg = request.GET.get('msg')
    uid = request.session['uid']
    payments = Payment.objects.filter(booking__worid=str(uid))
    today = d.today().strftime("%Y-%m-%d")
    return render(request, 'worker/workerviewpayment.html', {"abc": payments, "msg": msg, "today": today})

def deletepayment(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("ab")
    efg = Booking.objects.filter(id=id).delete()
    msg = "Deleted"
    return HttpResponseRedirect("/worker_home?msg="+msg)

######## // WORKER ########
######## CHAT ########

def user_chat_list(request):
    uid = request.session.get('uid')
    user = UserReg.objects.get(id=uid)
    # Get distinct workers that this user has approved or paid bookings with
    bookings = Booking.objects.filter(usrid=uid, status__in=["approved", "paid"])
    worker_ids = bookings.values_list('worid', flat=True).distinct()
    workers = WorkersReg.objects.filter(id__in=worker_ids)
    return render(request, 'user/user_chat_list.html', {'workers': workers})

def user_chat(request):
    uid = request.session.get('uid')
    worker_id = request.GET.get('worker_id')
    user = UserReg.objects.get(id=uid)
    worker = WorkersReg.objects.get(id=worker_id)
    if request.POST:
        message = request.POST.get('message', '').strip()
        if message:
            ChatMessage.objects.create(
                user=user,
                worker=worker,
                sender='user',
                message=message
            )
    messages = ChatMessage.objects.filter(user=user, worker=worker)
    return render(request, 'user/user_chat.html', {
        'messages': messages,
        'worker': worker,
        'worker_id': worker_id
    })

def worker_chat_list(request):
    wid = request.session.get('uid')
    worker = WorkersReg.objects.get(id=wid)
    # Get distinct users that booked this worker with approved or paid status
    bookings = Booking.objects.filter(worid=wid, status__in=["approved", "paid"])
    user_ids = bookings.values_list('usrid', flat=True).distinct()
    users = UserReg.objects.filter(id__in=user_ids)
    return render(request, 'worker/worker_chat_list.html', {'users': users})

def worker_chat(request):
    wid = request.session.get('uid')
    user_id = request.GET.get('user_id')
    worker = WorkersReg.objects.get(id=wid)
    user = UserReg.objects.get(id=user_id)
    if request.POST:
        message = request.POST.get('message', '').strip()
        if message:
            ChatMessage.objects.create(
                user=user,
                worker=worker,
                sender='worker',
                message=message
            )
    messages = ChatMessage.objects.filter(user=user, worker=worker)
    return render(request, 'worker/worker_chat.html', {
        'messages': messages,
        'user': user,
        'user_id': user_id
    })

######## // CHAT ########
