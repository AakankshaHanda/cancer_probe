"""myproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('help',views.help, name="help"),
    path('index',views.index, name="index"),
    path('aboutus',views.about,name="aboutus"),
    path('contact',views.contact, name="contact"),
    path('adminp',views.adminp, name="adminpanel"),
    path('bcancer',views.bcancer,name="bcancer"),
    path('ccancer',views.ccancer, name="ccancer"),
    path('passchange',views.passchange, name="passchange"),
    path('editpro', views.editpro, name="editprofile"),
    path('helpands',views.helpands, name="helpandsecurity"),
    path('login',views.login, name="login"),
    path('lcancer',views.lcancer, name="lcancer"),
    path('mprofile',views.mprofile, name="mprofile"),
    path('register', views.register, name="register"),
    path('review',views.review, name="review"),
    path('doctors', views.view_doctor, name="doctor"),
    path('hospitals',views.view_hospital, name="hospital"),
    path('NGO',views.view_NGO,name="NGO"),
    path('Visual',views.view_visual, name="Visual"),
    path('Visualbox', views.view_visualbox, name="Visualbox"),
    path('Visualbar', views.view_visualbar, name="Visualbar"),
    path('Visualgroupby', views.view_visualgroupby, name="Visualgroupby"),
    path('Visualbins', views.view_visualbins, name="Visualbins"),
    path('bplot', views.view_bplot, name="bplot"),
    path('maxmin', views.view_maxmin, name="maxmin"),
    path('ifelsebins', views.view_ifelsebins, name="ifelsebins"),
    path('lungdyn',views.view_lungdyn, name="lungdyn"),
    path('lungsm', views.view_lungsm, name="lungsm"),
    path('lungbar',views.view_lungbar, name="lungbar"),
    path('lungres',views.view_lungres, name="lungres"),
    path('box1', views.view_box1, name="box1"),
    path('lungbox1',views.view_lungbox1, name="lungbox1"),
    path('doctorsp',views.doctorsp,name="doctorsp"),
    path('breastcancerp',views.breastcancerp, name="breastcancerp"),
    path('bcanceroverview',views.bcanceroverview, name="bcanceroverview"),
    path('bcancerpreventions',views.bcancerpreventions, name="bcancerpreventions"),
    path('bcancersymptoms',views.bcancersymptoms, name="bcancersymptoms"),
    path('bcancervisual',views.bcancervisual, name="bcancervisual"),
    path('ccancerp', views.ccancerp, name="ccancerp"),
    path('ccanceroverview', views.ccanceroverview, name="ccanceroverview"),
    path('ccancerpreventions', views.ccancerpreventions, name="ccancerpreventions"),
    path('ccancersymptoms', views.ccancersymptoms, name="ccancersymptoms"),
    path('doctorspanelmain', views.doctorspanelmain, name="doctorspanelmain"),
    path('lcanceroverview', views.lcanceroverview, name="lcanceroverview"),
    path('lcancerpreventions', views.lcancerpreventions, name="lcancerpreventions"),
    path('lcancersymptoms', views.lcancersymptoms, name="lcancersymptoms"),
    path('lcancervisual',views.lcancervisual, name="lcancervisual"),
    path('lcancerprediction', views.lcancerprediction, name="lcancerprediction"),
    path('lcancermain', views.lcancer, name="lcancermain"),
    path('bcancermain', views.bcancer, name="bcancermain"),
    path('ccancermain', views.ccancer, name="ccancermain"),
    path('bcancerprediction', views.bcancerpredict, name="bcancerprediction"),
    path('forgotpassword',views.forgotpass,name="forgotpassword"),
    path('ccancerpred',views.ccancerpredict, name="ccancerpred"),
    
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

