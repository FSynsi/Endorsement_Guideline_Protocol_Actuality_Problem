from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import docx
from docx import Document
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from cryptography.fernet import Fernet
from six import b
import os
from os.path import dirname, join
# Create your views here.
from employee.models import dkey_request1
from managing_director.models import upload_product1


def managing_director(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        if uname == 'director' and password == 'director':
            return redirect("director_home")
    return render(request, 'managing_director/managing_director.html')

def director_home(request):
    para1=''
    if request.method == "POST" and request.FILES['work_requirements']:
        pname = request.POST.get('pname')
        duration = request.POST.get('duration')
        designation = request.POST.get('designation')
        work_requirements = request.FILES['work_requirements']
        fs = FileSystemStorage()
        filename = fs.save(work_requirements.name, work_requirements)
        print(filename)
        uploaded_file_url = fs.url(filename)
        ROOT_DIR = dirname(dirname(__file__))
        print(ROOT_DIR)
        output_path = join(ROOT_DIR, 'assests\media')
        print(output_path)
        fullpath=os.path.join(output_path,filename)
        print(fullpath)
        doc = docx.Document(fullpath)
        all_paras = doc.paragraphs
        len(all_paras)
        for para in all_paras:
            para1 = para1+para.text
        key = Fernet.generate_key()
        slogan = para1.encode()
        f = Fernet(key)
        coded_slogan = f.encrypt(slogan)
        upload_product1.objects.create(pname=pname, duration=duration, designation=designation,
                                       work_requirements=work_requirements,
                                        file_path=uploaded_file_url,fcontent=para1,enc_content=coded_slogan)
    return render(request, 'managing_director/director_home.html')

def viewkey_request(request):
    sts11="pending"
    keyrequest_details = dkey_request1.objects.filter(stauts=sts11)

    return render(request, 'managing_director/viewkey_request.html',{'keyrequest_details':keyrequest_details})

def generate_key1(request,pk):

    sts11 = "send"
    uname1 = User.objects.make_random_password(length=5, allowed_chars="01234567889")
    print(uname1)
    subject = "Decryption Key Details"
    text_content = ""
    objs = dkey_request1.objects.get(id=pk)
    uemail = objs.empemail
    print(uemail)
    html_content = "<br/><p>Your Decryption Key:<strong>" + str(uname1) + "<strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [uemail]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        dkey_request1.objects.filter(id=pk).update(stauts=sts11, dkey=uname1)


    return render(request, 'managing_director/generate_key1.html')