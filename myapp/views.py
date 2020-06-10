from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import doctors
from myapp.models import Review
from myapp.models import Reg
from myapp.models import Login
from myapp.models import Changepassword
from myapp.models import HandS
from myapp.models import Contact
from myapp.models import hospital
from myapp.models import NGO
from django.shortcuts import redirect
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import io
import base64
from PIL import Image, ImageDraw
import PIL, PIL.Image
import pickle
import numpy as np
from django.conf import settings
from django.core.mail import send_mail
from keras.models import load_model
from tensorflow import keras
from keras.preprocessing import image
# Create your views here.
def index(request):
    return HttpResponse("Hello")
def help(request):
    my_dict={}
    return render(request,'help.html',context=my_dict)
def index(request):
    my_dict={}
    return render(request,'index.html',context=my_dict)
def contact(request):
    if request.method=='POST':
           if request.POST.get('nm') and request.POST.get('mail') and request.POST.get('ph') and request.POST.get('msg'):
               post=Contact()
               post.name=request.POST.get('nm')
               post.email=request.POST.get('mail')
               post.phone=request.POST.get('ph')
               post.message=request.POST.get('msg')
               post.save()
           
               return render(request,'contact us.html')
    else:
               return render(request,'contact us.html') 


def about(request):
    my_dict={}
    return render(request,'about.html',context=my_dict)

def adminp(request):
    my_dict={}
    return render(request,'adminpanel.html',context=my_dict)
def bcancer(request):
    my_dict={}
    return render(request,'breastcancer.html',context=my_dict)
def ccancer(request):
    my_dict={}
    return render(request,'cervicalcancer.html',context=my_dict)
def passchange(request):
    if not request.session.has_key('email'):
        return redirect('/login/')
    if request.method=='POST':
        regi=Reg.objects.get(email=request.session['email'])
        oldp=request.POST.get('oldpass')
        newp=request.POST.get('psw')
        retypep=request.POST.get('npsw')
        print("old password",oldp)
        print(newp)
        print(retypep)
        if (newp==retypep):
             p=regi.password
             print("db password",p)
             if (oldp==p):
                 regi.password=newp
                 regi.save()
                 rest="Your Password has been changed successfully"
                 print("password updated!")
                 return render(request,'changepassword(1).html',{'rest':rest})
             else:
                 print("password not updated")
                 res="Invalid current password"
                 return render(request,'changepassword(1).html',{'res':res})
        else:
             res="Confirm password and new password don't match"
             return render(request,'changepassword(1).html',{'res':res})
    else:
        return render(request,'changepassword(1).html')
                       
def editpro(request):
    if not request.session.has_key('email'):
        return redirect ('/login/')
    userdetail=Reg.objects.get(email=request.session['email'])
    if request.method=='POST':
        detail=Reg.objects.get(email=request.POST.get('em'))
        detail.fname=request.POST.get('nm')
        detail.lname=request.POST.get('lm')
        detail.birthday=request.POST.get('dob')
        detail.save()
        data=Reg.objects.get(email=request.session['email'])
        return render(request,'Myprofile.html',{'user':data})
    else:
            return render(request,'editprofile.html.html',{'user':userdetail})
def helpands(request):
    if not request.session.has_key('email'):
        return redirect('/login/')
    if request.method=='POST':
          if request.POST.get('sub') and request.POST.get('txt'):
              post=HandS()
              post.subject=request.POST.get('sub')
              post.txtarea=request.POST.get('txt')
              post.save()
              return render(request,'helpandsupport.html')
    else:
              return render(request,'helpandsupport.html')
def login(request):
    if request.method=='POST':
        formpost=True
        us=request.POST.get('email')
        pw=request.POST.get('password')
        errormessage=""
        expert=Reg.objects.filter(email=us, password=pw)
        k=len(expert)
        if k>0:
            print("valid credentials")
            request.session['email']=us
            return render(request,'doctorspanelmain.html',{})
              
               
        else:      
            print("invalid credentials")
            errormessage="invalid credentials"
            return render(request,'login.html', {'formpost': formpost})
    else:
        formpost=False 
        return render(request,'login.html',{'formpost':formpost})





def forgotpass(request):
    if (request.method=='POST'):
        em=request.POST.get('email')
        user=Reg.objects.filter(email=em)
        if(len(user)>0):
            pw=user[0].password
            subject="Password"
            message="welcome. Your password is"+pw
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            send_mail(subject,message,email_from,recipient_list)
            rest="your password has been sent to your email. Please check"
            return render(request,'forgotpassword.html',{'rest':rest})
        else:
            res="The email id is not registered"
            return render(request,'forgotpassword.html',{'res':res})
    else:
        return render(request, 'forgotpassword.html')



def lcancer(request):
    my_dict={}
    return render(request,'lungcancer.html',context=my_dict)

def myprofile(request):
     if not request.session.has_key('email'):
         return redirect('/login/')
     userdetail= Reg.objects.get(email=request.session['email'])
     

     return render(request,'Myprofile.html',{'user':userdetail}) 
    
def register(request):
    if request.method=='POST':
            if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('birthday')and request.POST.get('password') and request.POST.get('cpassword'):
                post=Reg()
                post.fname=request.POST.get('fname')
                post.lname=request.POST.get('lname')
                post.email=request.POST.get('email')
                post.birthday=request.POST.get('birthday')
                post.password=request.POST.get('password')
                post.cpassword=request.POST.get('cpassword')
                post.save()
                return render(request,'register.html')
    else:
                return render(request,'register.html')
def review(request):
    if not request.session.has_key('email'):
        return redirect('/login/')
    if request.method=='POST':
           if request.POST.get('r') and request.POST.get('t'):
               post=Review()
               post.review=request.POST.get('r')
               post.txtarea=request.POST.get('t')
               post.save()
               return render(request,'review.html')
    else:
               return render(request,'review.html')
def view_doctor(request):
    dc=doctors.objects.all()
    return render(request,'alldoctor.html',{'dc': dc})
def view_hospital(request):
    hs=hospital.objects.all()
    return render(request,'allhospitals.html',{'hs':hs})
def view_NGO(request):
    ng=NGO.objects.all()
    return render(request,'allngo.html',{'ng':ng})
def view_visual(request):
    if request.method=='POST':
         t=request.POST.get('type')
         print(t)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
         df1= df.iloc[:,2:5]
         df1.plot.box(grid=True,figsize=(7,7),title='BREAST CANCER')
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})

    else:
        return render(request,'visual.html')

def view_visualbox(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         y=request.POST.get('t2')
         z=request.POST.get('t3')
         print(x)
         print(y)
         print(z)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
  

         df1=df.groupby('diagnosis')[x,y,z].sum()
         df1=df1.transpose()
         explode = (0, 0.1, 0)
         df1.plot.pie(radius=1.2,subplots=True,explode=explode,autopct='%1.1f%%',figsize=(7,7),
         labeldistance=1.1,title='Breast Cancer\n (B-Benign M-Malignant)',fontsize=10)

         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'visualbox.html')


def view_visualbar(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         y=request.POST.get('t2')
         print(x)
         print(y)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
  
         ax=df.groupby('diagnosis')[x,y].sum().plot.bar(rot=360, title='graph of '+x+'  and '+y)
         ax.set_facecolor('bisque')

         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'visualbar.html')


def view_visualgroupby(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
  
         ax=df.groupby('diagnosis')[x].sum().plot.bar(grid=True, rot=360, title='graph of '+x , color='skyblue')
         ax.set_facecolor('Black')

         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'visualgroupby.html')



def view_visualbins(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
  
         r=[0,15,30]
         df['r']= pd.cut(df[x], bins=r)
         df.groupby('r')[x].sum().plot.bar( grid=True, rot=360, title="graph of"          +x,figsize=(7,8), color='Pink')

         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'visualgroupby.html')


def view_bplot(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
  
         
         ax=df.loc[:,x].plot.box()
         ax.set_facecolor('peachpuff')
         ax.set_title('BREAST CANCER \n'+x  , color='maroon' ,  fontsize=15)
         ax.set_ylabel('Range' , color='maroon',fontsize=13)

         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'bplot.html')

def view_box1(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
         ax=df.boxplot(column= x, by='diagnosis',rot=360, color='black')
         ax.set_facecolor('pink')

         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'box1.html')









def view_maxmin(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
         min=df.loc[:,x].min()
         max=df.loc[:,x].max()
         df= df[df[x].isin([max, min])]
         df=df.set_index('diagnosis')
         ax=df.loc[:,x].plot.bar(grid=True,title='BRREAST CANCER \nMax- Min of '+x,rot=360 , color='skyblue')
         ax.set_facecolor('gray')
         
         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'maxmin.html')


def view_ifelsebins(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('bdata.csv')
         r=[0,15,30]
         a=[200,400,600,800,1000,1200,1400,1600,1800]
         p=[0,30,60,90.120,150,180,210]
         tm=[10,20,30,40]
         sm=[0.05,0.10,0.14,0.17]
         cm=[0.19,0.21,0.26,0.29,0.31,0.35]
         c=[0,0.12,0.22,0.32,0.43]
         cp=[0,0.05,0.01,0.15,0.21]
         sym=[0.10,0.15,0.25,0.31]
         fd=[0.04,0.06,0.10]


         if (x=='radius_mean'):

             bins=r
         elif (x=='area_mean'):
             bins=a
         elif (x=='perimeter_mean'):
             bins=p
         elif(x=='texture_mean'):
             bins=tm
         elif(x=='smoothness_mean'):
             bins=sm
         elif(x=='compactness_mean'):
             bins=cm
         elif(x=='concavity_mean'):
             bins=c
         elif(x=='concave points_mean'):
             bins=cp
         elif(x=='symmetry_mean'):
             bins=sym
         elif(x=='fractal_dimension_mean'):
             bins=fd
       
         df['new_col'] = pd.cut(df[x], bins= bins )
         df.groupby('new_col')[x].sum().plot.barh(grid=True,title='Sum of texture mean within certain ranges of '+x)

         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'ifelsebins.html')


def view_lungdyn(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('lung_cancer_examples.csv')
         age=[0,15, 30, 40]

         df['age']= pd.cut(df[x], bins=age)
         df1=df.groupby('age')[x].sum().plot.bar(grid=True, rot=360,title='LUNG CANCER graph of'     +x, color='violet' )
         

         
         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'lungdyn.html')


def view_lungsm(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('lung_cancer_examples.csv')
         sm=[0,25,35]

         df['sm']=pd.cut(df[x],bins=sm)
         df1=df.groupby('sm')[x].sum().plot.bar(grid=True, rot=360,title='LUNG CANCER graph of Smokes with   '+x, color='pink')



         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'lungsm.html')




def view_lungbar(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         y=request.POST.get('t2')
         print(x)
         print(y)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('lung_cancer_examples.csv')
         
         ax=df.groupby('Result')[x,y].sum().plot.bar(grid=True, rot=360, title='graph of Result with  '+x+'  and '+y)
         ax.set_facecolor('bisque')



         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'lungbar.html')




def view_lungres(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('lung_cancer_examples.csv')
         
         ax=df.groupby('Result')[x].sum().plot.bar(grid=True, rot=360, title='graph of Result with  '+x , color='skyblue')
         ax.set_facecolor('Black')



         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'lungres.html')



def view_lungbox1(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('lung_cancer_examples.csv')
         
         ax=df.boxplot(grid=True, column= x, by='Result',rot=360, color='black')
         ax.set_facecolor('pink')


         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'lungbox1.html')


def doctorsp(request):
    my_dict={}
    return render(request,'doctorspanel.html',context=my_dict)

def breastcancerp(request):
    my_dict={}
    return render(request,'bcancerDOCTORSPANEL.html',context=my_dict)

def bcanceroverview(request):
    my_dict={}
    return render(request,'bcancerOVERVIEW.html',context=my_dict)

def bcancerpreventions(request):
    my_dict={}
    return render(request,'bcancerPREVENTIONS.html',context=my_dict)

def bcancersymptoms(request):
    my_dict={}
    return render(request,'bcancerSYMTOMS.html',context=my_dict)

def bcancervisual(request):
    my_dict={}
    return render(request,'bcancerVISUALIZATIONS.html',context=my_dict)
def ccancerp(request):
    my_dict={}
    return render(request,'ccancerDOCTORSPANEL.html',context=my_dict)

def ccanceroverview(request):
    my_dict={}
    return render(request,'ccancerOVERVIEW.html',context=my_dict)

def ccancerpreventions(request):
    my_dict={}
    return render(request,'ccancerPREVENTIONS.html',context=my_dict)

def ccancersymptoms(request):
    my_dict={}
    return render(request,'ccancerSYMPTOMS.html',context=my_dict)


def ccancervis(request):
    my_dict={}
    return render(request,'ccancerVISUALIZATIONS.html',context=my_dict)

def doctorspanelmain(request):
    my_dict={}
    return render(request,'doctorspanelmain.html',context=my_dict)

def lcanceroverview(request):
    my_dict={}
    return render(request,'lcancerOVERVIEW.html',context=my_dict)

def lcancerpreventions(request):
    my_dict={}
    return render(request,'lcancerPREVENTION.html',context=my_dict)

def lcancersymptoms(request):
    my_dict={}
    return render(request,'lcancerSYMPTOMS.html',context=my_dict)

def lcancervisual(request):
    my_dict={}
    return render(request,'lcancerVISULAIZATIONS.html',context=my_dict)

def lcancerprediction(request):
    if request.method=='POST':
         Age = request.POST.get('ag')
         Smokes=request.POST.get('sm') 
         AreaQ= request.POST.get('AQ')
         Alkhol=request.POST.get('Al')
         pkl_filename = "pickle_model.pkl"
         with open(pkl_filename, 'rb') as file:
             pickle_model = pickle.load(file)
         dataset=pd.read_csv('lung_cancer_examples.csv')
         x=dataset.iloc[:,[2,3,4,5]]
         y=dataset.iloc[:,6]
         
#label encoder and one hot encoder
         from sklearn.preprocessing import LabelEncoder, OneHotEncoder
         labelencoder_y=LabelEncoder()
         y=labelencoder_y.fit_transform(y)
#dividing into training and testing
         from sklearn.model_selection import train_test_split
         x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
#feature scaling
         print("before",x_test.shape)
         x_test=np.append(x_test,[[Age,Smokes,AreaQ,Alkhol]],axis=0)
         print("after",x_test.shape)
         from sklearn.preprocessing import StandardScaler
         sc=StandardScaler()
         x_train=sc.fit_transform(x_train)
         x_test=sc.transform(x_test)
         from sklearn.tree import DecisionTreeClassifier
         classifier=DecisionTreeClassifier(criterion='gini',random_state=0)
         classifier.fit(x_train,y_train)
         y_pred=classifier.predict(x_test)
         if y_pred[15]==1:
             return render(request,'detected.html')
         else:
             return render(request,'notdetected.html')

         
    else:
     my_dict={}
     return render(request,'lungprediction.html',context=my_dict)

def bcancerpredict(request):
    if request.method=='POST':
         radius_mean = request.POST.get('r_mean')
         texture_mean=request.POST.get('tx_mean') 
         perimeter_mean= request.POST.get('p_mean')
         area_mean=  request.POST.get('ar_mean')
         smoothness_mean = request.POST.get('smo_mean')
         compactness_mean=request.POST.get('compact_mean') 
         concavity_mean= request.POST.get('concavity_mean')
         concave_points_mean= request.POST.get('concavept_mean')
         symmetry_mean = request.POST.get('sym_mean')
         fractal_dimension_mean=request.POST.get('fd_mean') 
         radius_se= request.POST.get('r_se')
         texture_se=request.POST.get('tx_se')
         perimeter_se=request.POST.get('p_se')
         area_se=request.POST.get('a_se')
         smoothness_se=request.POST.get('smo_se')
         compactness_se=request.POST.get('compact_se')
         concavity_se=request.POST.get('concavity_se')
         concave_points_se=request.POST.get('concavept_se')
         symmetry_se=request.POST.get('sym_se')
         fractal_dimension_se=request.POST.get('fd_se')
         radius_worst=request.POST.get('r_worst')
         texture_worst=request.POST.get('tx_worst')
         perimeter_worst=request.POST.get('p_worst')
         area_worst=request.POST.get('a_worst')
         smoothness_worst=request.POST.get('smo_worst')
         compactness_worst=request.POST.get('compact_worst')
         concavity_worst=request.POST.get('concavity_worst')
         concave_points_worst=request.POST.get('concavepts_worst')
         symmetry_worst=request.POST.get('sym_worst')
         fractal_dimension_worst=request.POST.get('fd_worst')
         pkl_filename = "pickle_model11.pkl"
         with open(pkl_filename, 'rb') as file:
             pickle_model11 = pickle.load(file)
         classifier=pickle_model11
         dataset=pd.read_csv('bdata.csv')
         x=dataset.iloc[:,2:32]
         y=dataset.iloc[:,1]
         print("col",x.dtypes)
         print("before",x.shape)
         x=np.append(x,[[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,
         concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,
         compactness_se,
         concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,
         smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]],axis=0)
         print("after",x.shape)

#labelencoder and one hot encoder
         from sklearn.preprocessing import LabelEncoder, OneHotEncoder
         labelencoder_x=LabelEncoder()
         x[:,1]=labelencoder_x.fit_transform(x[:,1])
         

#splitting to training and  testing
        
         """X_test=np.append(X_test,[[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,
         concavity_mean,concave_points_mean,symmetry_mean,radius_se,perimeter_se,area_se,smoothness_se,compactness_se,
         concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,perimeter_worst,area_worst,
         smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]],axis=0)"""
         #print('after',X_test.shape)
         from sklearn.preprocessing import StandardScaler
         sc=StandardScaler()
         x=sc.fit_transform(x)
        # x_test=sc.transform(x_test)
         
#predicting new result
         y_pred=classifier.predict(x)
         if y_pred[569]==1:
             return render(request,'detected.html')
         else:
             return render(request,'notdetected.html')

    else:
     my_dict={}
     return render(request,'bcancerprediction.html',context=my_dict)





def ccancerpredict(request):
    if request.method=='POST':
         Age=request.POST.get('age')
         Number_of_sexual_partners = request.POST.get('num')
         First_sexual_intercourse=request.POST.get('fs') 
         Num_of_pregnancies= request.POST.get('np')
         Smokes=  request.POST.get('smk')
         years = request.POST.get('yrs')
         Smokespacks=request.POST.get('smo_packs') 
         Hormonal_Contra= request.POST.get('hc')
         Hormonal_Contra_years= request.POST.get('hcy')
         IUD = request.POST.get('iud')
         IUD_years=request.POST.get('iudy') 
         STDs= request.POST.get('std')
         STDs_number=request.POST.get('stdy')
         STDs_cond=request.POST.get('stdc')
         STDs_cervical_cond=request.POST.get('stdcc')
         STDs_vaginal_cond=request.POST.get('stdvc')
         STDs_v_perineal_cond=request.POST.get('stdv')
         STDs_syphilis=request.POST.get('stds')
         STDs_pel_infla_disease=request.POST.get('stdpe')
         STDs_gen_herpes=request.POST.get('stdge')
         STDs_molluscum_contag=request.POST.get('stdmo')
         STDs_AIDS=request.POST.get('stdai')
         STDs_HIV=request.POST.get('stdhi')
         STDs_HepatitisB=request.POST.get('stdhb')
         STDs_HPV=request.POST.get('stdhp')
         STDs_Num_of_diagnosis=request.POST.get('stdnum')
         Dx_Cancer=request.POST.get('dc')
         Dx_CIN=request.POST.get('dcin')
         Dx_HPV=request.POST.get('dhp')
         Dx=request.POST.get('d')
         Hinselmann=request.POST.get('hin')
         Schiller=request.POST.get('sch')
         Citology=request.POST.get('cit')
         pkl_filename = "pickle_modelcervical.pkl"
         with open(pkl_filename, 'rb') as file:
             pickle_modelcervical = pickle.load(file)
         classifier=pickle_modelcervical
         dataset=pd.read_csv('cervical.csv')
         dataset=dataset.dropna()
         
         def abc(x):
             if x=='?':
                 return 'NaN'
             else:
                 return x
                 
         from sklearn.impute import SimpleImputer

         imputer=SimpleImputer(missing_values=np.NaN,strategy="mean")
         imputer=imputer.fit(dataset.iloc[:,1:25])
         dataset.iloc[:,1:25]=imputer.transform(dataset.iloc[:,1:25])
         dataset = dataset.dropna()
         col=[0,3,4,5,6,8,9,10,11,12,13,16,17,19,22,25,26,27,28,29,30,31,32]
         x=dataset.iloc[:,0:33].values
         y=dataset.iloc[:,33].values
         
         print("before",x.shape)
         x=np.append(x,[[Age,Number_of_sexual_partners,First_sexual_intercourse,Num_of_pregnancies,Smokes, years,Smokespacks,
         Hormonal_Contra,Hormonal_Contra_years,IUD,IUD_years,STDs,STDs_number,
         STDs_cond,STDs_cervical_cond,STDs_vaginal_cond,
         STDs_v_perineal_cond,
         STDs_syphilis,STDs_pel_infla_disease,STDs_gen_herpes,STDs_molluscum_contag,STDs_AIDS,STDs_HIV,
         STDs_HepatitisB,STDs_HPV,
         STDs_Num_of_diagnosis,
         Dx_Cancer,Dx_CIN,Dx_HPV,Dx,Hinselmann,Schiller,Citology]],axis=0)
         print("after",x.shape)
         print(x[858])
         from sklearn.preprocessing import StandardScaler
         sc=StandardScaler()
         x=sc.fit_transform(x)
        # x_test=sc.transform(x_test)
         
#predicting new result
         y_pred=classifier.predict(x)
         if y_pred[858]==1:
             return render(request,'detected.html')
         else:
             return render(request,'notdetected.html')

         

    else:
     my_dict={}
     return render(request,'cervicalcancerprediction.html',context=my_dict)



def logout(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    del request.session['email']
    return redirect('/login')



def handle_uploaded_file(f,name):
    destination = open(name, 'wb+')
    for chunk in f.chunks():
         destination.write(chunk)
         destination.close()

def skinc(request):
    if request.method=='POST':
        f=request.FILES['sentFile'] 
        handle_uploaded_file(f,f.name) 
        classifier=keras.models.load_model('skincancer.h5')  
        test_image=image.load_img(f.name,target_size=(64,64))  
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image,axis=0)
        result=classifier.predict(test_image)
        print(result)
        if result[0][0]>=0.5:
            return render(request,'detected.html')
        else:
            return render(request,'notdetected.html')
    else:
         return render(request,'skincancer.html')


def vis1(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         x="Smokes_packs_years"
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('cervical.csv')
         
         df=df.replace('?',0).astype(float)
         df=df.astype(int)
         b=[10,20,30,40,50,60,70,80,90]  
         df['age-grp'] =pd.cut(df['Age'] ,bins=b)    
         df.groupby('age-grp')[x].sum().plot.bar(title='Grouping of Age groups based on -'+x) 
        
         
        
         print("after frouping",df.shape )

         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'cervis1.html')



def vis2(request):
     if request.method=='POST':
         x = request.POST.get('t1')
         print(x)
         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
         matplotlib.rcParams['axes.labelsize'] = 14
         matplotlib.rcParams['xtick.labelsize'] = 8
         matplotlib.rcParams['ytick.labelsize'] = 12
         matplotlib.rcParams['text.color'] = 'k'
         df = pd.read_csv('cervical.csv')
         
         b=[10,20,30,40,50,60,70,80,90]  
         df['age-grp'] =pd.cut(df['Age'] ,bins=b)    
         df.groupby(['age-grp','Biopsy'])[x].sum().plot.barh(grid=True,title='Grouping of Age groups ans Biopsy based on -'+x)

         buf = io.BytesIO()
         plt.margins(0.8)
# Tweak spacing to prevent clipping of tick-labels
         plt.subplots_adjust(bottom=0.35)
         plt.savefig(buf, format='png')

         fig.savefig('abc.png')

         plt.close(fig)
         image = Image.open("abc.png")
         draw = ImageDraw.Draw(image)

         image.save(buf, 'PNG')
         content_type="Image/png"
         buffercontent=buf.getvalue()


         graphic = base64.b64encode(buffercontent)
         return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
         return render(request,'cervis2.html')


def predictormain(request):
    my_dict={}
    return render(request,'predictor.html',context=my_dict)


def news(request):
    my_dict={}
    return render(request,'newsandresearch.html',context=my_dict)





























     



