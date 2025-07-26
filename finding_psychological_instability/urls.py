"""finding_psychological_instability URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from finding_psychological_instability import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static
from Remote_User import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    path(r'^$', remoteuser.login, name="login"),
    path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    path(r'^Search_PsychologyDataSets_Details/$', remoteuser.Search_PsychologyDataSets_Details, name="Search_PsychologyDataSets_Details"),
    path(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path(r'^Add_DataSet_Details/$', remoteuser.Add_DataSet_Details, name="Add_DataSet_Details"),
    path(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    path(r'^Search_DataSets/$', serviceprovider.Search_DataSets, name="Search_DataSets"),
    path(r'^View_Depressed/$', serviceprovider.View_Depressed, name="View_Depressed"),
    path(r'^Predict_Psychological_Instability/$', serviceprovider.Predict_Psychological_Instability, name="Predict_Psychological_Instability"),
    path(r'^View_psychologyDataSets_Details/$', serviceprovider.View_psychologyDataSets_Details, name="View_psychologyDataSets_Details"),
    path(r'^View_Stressed/$', serviceprovider.View_Stressed, name="View_Stressed"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
