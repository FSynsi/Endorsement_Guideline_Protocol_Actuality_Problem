from django.shortcuts import render, redirect
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from django.utils.encoding import smart_str

from employee.models import employee_reg, dkey_request1, transportation1, payment1
from managing_director.models import upload_product1
import re
from django.db.models import Subquery
import os
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

def employee_index(request):

     return render(request, 'employee/employee_index.html')

def growth_story(request):

    return render(request, 'employee/growth_story.html')

def history(request):

    return render(request, 'employee/history.html')
def board_of_directors(request):

    return render(request, 'employee/board_of_directors.html')

def material_management(request):

    return render(request, 'employee/material_management.html')

def health_safety(request):

    return render(request, 'employee/health_safety.html')

def environment(request):

    return render(request, 'employee/environment.html')

def carbon_management(request):

    return render(request, 'employee/carbon_management.html')

def energy_center(request):

    return render(request, 'employee/energy_center.html')

def notices(request):

    return render(request, 'employee/notices.html')

def policies(request):

    return render(request, 'employee/policies.html')

def press_release(request):

    return render(request, 'employee/press_release.html')

def employee_login(request):

    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = employee_reg.objects.get(uname=uname, password=pswd)
            request.session['eid'] = check.id
            request.session['ename'] = check.uname
            request.session['emp_email'] = check.email
            request.session['designation'] = check.designation
            return redirect('employee_home')
        except:
            pass
        return redirect('employee_login')

    return render(request, 'employee/employee_login.html')

def employee_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        if designation=="senior_engineer":
            group_password="SEE004"
        elif designation=="junior_engineer":
            group_password = "JEE101"
        elif designation == "contractors":
            group_password = "CON203"
        elif designation == "agencies":
            group_password = "AGN899"
        elif designation == "subcontractors":
            group_password = "SUC987"
        elif designation == "tunnel_operator":
            group_password = "TUN900"
        elif designation == "apprentices":
            group_password = "APPR876"
        elif designation == "general_manager":
            group_password = "GEM983"
        elif designation == "chief_general_manager":
            group_password = "CGM564"
        elif designation == "production_general_manager":
            group_password = "PGM555"
        elif designation == "construction_general_manager":
            group_password = "CGM622"
        elif designation == "deputy_general_manager":
            group_password = "DGM756"
        elif designation == "financial_deputy_general_manager":
            group_password = "FDM545"
        elif designation == "general_manager_human_resource":
            group_password = "GMR444"
        else:
            group_password = "DGMP987"

        subject = "Group Password"
        text_content = ""

        html_content = "<br/><p>Your Group Password Is:<strong>" + str(group_password) + "<strong></p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        if msg.send():
            employee_reg.objects.create(fname=first_name, lname=last_name, email=email, designation=designation, gender=gender,
                                    uname=uname,password=password,group_password1=group_password)
        return redirect('employee_login')
    return render(request, 'employee/employee_register.html')

def employee_home(request):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)
    if request.method == "POST":
        gpassword = request.POST.get('gpassword')
        total_filedetails = employee_reg.objects.filter(id=emp_id,group_password1=gpassword)
        return redirect("view_files")
    return render(request, 'employee/employee_home.html')

def view_files(request):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)
    if upload_product1.objects.filter(designation__contains=emp_designation):
        return redirect("view_files1")
    else:
        return redirect("view_files2")

    return render(request, 'employee/view_files.html',{'objects':total_filedetails,'emp_designation':emp_designation})

def download_project(request,pk):
    emp_id = request.session['eid']
    emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    objspath = upload_product1.objects.get(id=pk)
    fpath1 = objspath.file_path
    print(fpath1)
    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath1)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='vnd.ms-word')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested file was not found in our server.')
    return redirect("employee_home")
    return render(request, 'employee/download_project.html')

def share_to_employee(request,pk):
    return render(request, 'employee/share_to_employee.html')

def view_files1(request):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)
    total_filedetails=upload_product1.objects.filter(designation__contains=emp_designation)
    return render(request, 'employee/view_files1.html',{'objects': total_filedetails, 'emp_designation': emp_designation})

def view_files2(request):
    designation1 = ''
    des1 = ''
    des2 = ''
    pname1 = ''
    emp_id = request.session['eid']
    emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    emp_designation = request.session['designation']
    print(emp_designation)
    total_filedetails=upload_product1.objects.all()
    return render(request, 'employee/view_files2.html',{'objects': total_filedetails, 'emp_designation': emp_designation})

def decrypt1(request,pk):
    keyresult22=''
    fileid=''
    emp_id = request.session['eid']
    emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    print(emp_email)
    emp_designation = request.session['designation']
    objspath1 = upload_product1.objects.get(id=pk)
    unid = objspath1.id
    print(unid)
    request.session['fid1']=unid
    sts11 = "send"
    sts22 = "deactivate"
    if request.method == "POST":
        dkey1 = request.POST.get("dkey")
        if dkey_request1.objects.filter(empid=emp_id, dkey=dkey1, stauts=sts11):
            keyresult=dkey_request1.objects.filter(empid=emp_id, dkey=dkey1, stauts=sts11)
            for t11 in keyresult:
                fileid = t11.fileid
            keyresult22=upload_product1.objects.filter(id=fileid)
            dkey_request1.objects.filter(empid=emp_id, dkey=dkey1, stauts=sts11).update(stauts=sts22)
        else:
            return redirect("decrypt_fail")

    return render(request, 'employee/decrypt1.html',{'keyresult22':keyresult22})




def dkey_request(request):
    emp_id = request.session['eid']
    emp_name = request.session['ename']
    emp_email = request.session['emp_email']
    print(emp_email)
    emp_designation = request.session['designation']
    fid1 = request.session['fid1']
    print(fid1)
    sts1 = "pending"
    key1 = "pending"
    dkey_request1.objects.create(empid=emp_id,empname=emp_name,empemail=emp_email,emp_designation=emp_designation,
                                 fileid=fid1,stauts=sts1,dkey=key1)

    return render(request, 'employee/dkey_request.html')

def decrypt_fail(request):

    return render(request, 'employee/decrypt_fail.html')

def upload_transportation(request):
    if request.method == "POST":
        transport_no = request.POST.get("transport_no")
        project_name = request.POST.get("project_name")
        send_place = request.POST.get("send_place")
        transportation1.objects.create(transport_no=transport_no, project_name=project_name, send_place=send_place)
    return render(request, 'employee/upload_transportation.html')

def payment(request):
    if request.method == "POST":
        project_name = request.POST.get("project_name")
        payment = request.POST.get("payment")

        payment1.objects.create(project_name=project_name, payment=payment)
    return render(request, 'employee/payment.html')