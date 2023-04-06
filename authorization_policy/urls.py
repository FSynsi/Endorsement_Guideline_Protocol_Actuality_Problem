"""authorization_policy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
#from django.conf.urls import url
from django.conf.urls.static import static
from employee import views as employeeviews
from managing_director import views as managingdirectorviews
from authorization_policy import settings
from projectadmin import views as projectadminviews
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',employeeviews.employee_index, name="employee_index"),
    re_path(r'^growth_story/$',employeeviews.growth_story, name="growth_story"),
    re_path(r'^history/$',employeeviews.history, name="history"),
    re_path(r'^board_of_directors/$',employeeviews.board_of_directors, name="board_of_directors"),
    re_path(r'^material_management/$',employeeviews.material_management, name="material_management"),
    re_path(r'^health_safety/$',employeeviews.health_safety, name="health_safety"),
    re_path(r'^environment/$',employeeviews.environment, name="environment"),
    re_path(r'^carbon_management/$',employeeviews.carbon_management, name="carbon_management"),
    re_path(r'^energy_center/$',employeeviews.energy_center, name="energy_center"),
    re_path(r'^notices/$',employeeviews.notices, name="notices"),
    re_path(r'^policies/$',employeeviews.policies, name="policies"),
    re_path(r'^press_release/$',employeeviews.press_release, name="press_release"),
    re_path(r'^employee_login/$',employeeviews.employee_login, name="employee_login"),
    re_path(r'^employee_register/$',employeeviews.employee_register,name="employee_register"),
    re_path(r'^employee_home/$',employeeviews.employee_home,name="employee_home"),
    re_path(r'^view_files/$',employeeviews.view_files,name="view_files"),
    re_path(r'^view_files1/$',employeeviews.view_files1,name="view_files1"),
    re_path(r'^view_files2/$',employeeviews.view_files2,name="view_files2"),
    re_path(r'^download_project/(?P<pk>\d+)/$',employeeviews.download_project,name="download_project"),
    re_path(r'^share_to_employee/(?P<pk>\d+)/$',employeeviews.share_to_employee,name="share_to_employee"),
    re_path(r'^decrypt1/(?P<pk>\d+)/$',employeeviews.decrypt1,name="decrypt1"),
    re_path(r'^dkey_request/$',employeeviews.dkey_request,name="dkey_request"),
    re_path(r'^decrypt_fail/$',employeeviews.decrypt_fail,name="decrypt_fail"),
    re_path(r'^upload_transportation/$',employeeviews.upload_transportation,name="upload_transportation"),
    re_path(r'^payment/$',employeeviews.payment,name="payment"),

    re_path(r'^managing_director/$',managingdirectorviews.managing_director,name="managing_director"),
    re_path(r'^director_home/$',managingdirectorviews.director_home,name="director_home"),
    re_path(r'^viewkey_request/$',managingdirectorviews.viewkey_request,name="viewkey_request"),
    re_path(r'^generate_key1/(?P<pk>\d+)/$',managingdirectorviews.generate_key1,name="generate_key1"),


    re_path(r'^projectadmin_login/$',projectadminviews.projectadmin_login, name="projectadmin_login"),
    re_path(r'^admin_home/$',projectadminviews.admin_home, name="admin_home"),
    re_path(r'^employee_details/$',projectadminviews.employee_details, name="employee_details"),
    re_path(r'^transportation_details/$',projectadminviews.transportation_details, name="transportation_details"),
    re_path(r'^payment_details/$',projectadminviews.payment_details, name="payment_details"),
    re_path(r'^admindownload_project/(?P<pk>\d+)/$',projectadminviews.admindownload_project,name="admindownload_project"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
