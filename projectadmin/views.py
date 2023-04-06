from django.shortcuts import render,redirect

# Create your views here.
from employee.models import employee_reg, payment1, transportation1
from managing_director.models import upload_product1
from django.utils.encoding import smart_str
from django.http import HttpResponse, HttpResponseNotFound


def projectadmin_login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        if uname == 'admin' and password == 'admin':
            return redirect("admin_home")
    return render(request, 'projectadmin/projectadmin_login.html')

def admin_home(request):
    project_details = upload_product1.objects.all()
    return render(request, 'projectadmin/admin_home.html',{'project_details':project_details})

def employee_details(request):
    employee_details = employee_reg.objects.all()
    return render(request, 'projectadmin/employee_details.html',{'employee_details':employee_details})

def transportation_details(request):
    transportation_details = transportation1.objects.all()
    return render(request, 'projectadmin/transportation_details.html',{'transportation_details':transportation_details})

def payment_details(request):
    payment_details = payment1.objects.all()
    return render(request, 'projectadmin/payment_details.html',{'payment_details':payment_details})

def admindownload_project(request,pk):

    objspath = upload_product1.objects.get(id=pk)
    fpath1 = objspath.file_path
    print(fpath1)
    fname11 = objspath.work_requirements
    print(fname11)
    response = HttpResponse(
        content_type='application/force-download')  # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(fname11)
    response['X-Sendfile'] = smart_str(fpath1)
    return response
    return render(request, 'projectadmin/admindownload_project.html')
