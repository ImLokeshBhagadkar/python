from django.shortcuts import render
from django.core.mail import send_mail
import mysql.connector as sql
#global variable

fn = ''
ln = ''
s = ''
em = ''
pwd = ''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",password="",database="website")
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=="first_name":
                fn = value
            if key=="last_name":
                ln = value
            if key=="sex":
                s = value
            if key=="email":
                em = value
            if key=="password":
                pwd = value
        c = "insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
        send_mail(
    'Account Verification',
    'Ur account is crested.',
    'bhagadkar.bh@gmail.com',
    [em],
    fail_silently=False,)
    return render(request,'signup_page.html')
