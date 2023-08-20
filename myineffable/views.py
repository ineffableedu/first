from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import CentreRegisterAdmin,CentreRegisterStudent
# Create your views here.
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib import messages


def index(request):
    return render(request,"index.html")
    
def adminlogin(request):
    return render(request,"adminlogin.html")




def authadmin_validation(request):
    adminuser=request.POST['adminuser']
    adminpassword=request.POST['adminpassword']
    msg=''
    try:
        print("1"*8)
        # adm=AdminLogin.objects.get(adminuser=adminuser,adminpassword=adminpassword)
        print(adminuser)
        print(adminpassword)
        if adminuser == "ineffable@gmail.com" and adminpassword == "ineffable123@":
            print("3"*8)

            request.session['adminid']=adminuser
            request.session['adminpassword']=adminpassword
            # msg='Valid user'
            return render(request,"admindashboard.html")

        else:
            msg='Invalid admin user'
            return render(request,"adminlogin.html",{'msg':msg})

    except ObjectDoesNotExist:
        print("2"*8)
        msg='Invalid admin user'
        return render(request,"adminlogin.html",{'msg':msg})



def admindashboard(request):
    return render(request,"admindashboard.html")



#Add customer
def admin_centerregistration(request):
    try:
        if request.session['adminid']:
            owner_name=request.POST['owner_name']
            center_email=request.POST['center_email']
            center_mobile=request.POST['center_mobile']
            center_id=request.POST['center_id']
            center_name=request.POST['center_name'],
            center_address=request.POST['center_address'],
            print(center_email,center_mobile,center_id,center_name,center_address)
            msg=''
            try:
            #msg=''
                ads=CentreRegisterAdmin.objects.get(center_id=center_id)
                if ads is not None:
                    msg='This center already registered..please try another email id!'
                    return render(request,"admindashboard.html",{'msg':msg})
                    #return HttpResponse('already registered')
            except ObjectDoesNotExist:
                center_photo=request.FILES['center_photo']
                print(center_photo)
                if request.method == 'POST' and request.FILES['center_photo']:
                    center_photo = request.FILES['center_photo']
                    fs = FileSystemStorage()
                    filenameprofile = fs.save(center_photo.name,center_photo)
                    center_photo = fs.url(filenameprofile)
                    msg=''
                    c_a_c=CentreRegisterAdmin(
                        center_id=center_id,
                        center_name=center_name[0],
                        center_address=center_address[0],
                        center_mobile=center_mobile,
                        center_email=center_email,
                        centerdatetime=datetime.datetime.today(),
                        center_photo=center_photo,
                        owner_name=owner_name,
                        center_password=12345678
                    )
                    c_a_c.save()
                    # msg='Customer Added succussfully'
                    # return render(request,"adminzone/index.html",{'msg':msg})
                    messages.info(request,'Center Added succussfully')
                    return redirect('admindashboard')
                else:
                    pass
    except:
        HttpResponse("You are not authorized!")


def  center_registration(request):
    return render(request,"center_registration.html")



def search_center(request):
    # Centerregister=CentreRegisterAdmin.objects.all()
    # return render(request,"search_center.html",{'Centerregister':Centerregister})
    return render(request,"search_center.html")


def center_authontication_login(request):
    
    centeruser=request.POST['centeruser']
    centerpassword=request.POST['centerpassword']
    msg=''
    try:
        # print("1"*8)
        sdfgh=CentreRegisterAdmin.objects.get(center_id=centeruser,center_password=centerpassword)
        if sdfgh is not None:

            print("3"*8)
            request.session['centeruser']=centeruser
            request.session['centerpassword']=centerpassword
            # msg='Valid user'
            return render(request,"centerdashboard.html")

        else:
            msg='Invalid center user'
            return render(request,"center_login.html",{'msg':msg})

    except ObjectDoesNotExist:
        print("2"*8)
        msg='Invalid center user'
        return render(request,"center_login.html",{'msg':msg})



def center_login(request):
    return render(request,"center_login.html")

def centerdashboard(request):
    return render(request,"centerdashboard.html")

def centerstudentregister(request):
    try:
        if request.session['centeruser']:
            try:
                from django.db.models import Max
                print("1"*8)
                crl=CentreRegisterStudent.objects.all().aggregate(Max('rollno'))
                crl2=crl['rollno__max']
                print(crl2)
                print("2"*8)
                if int(crl2) >= 100001:
                    print("4"*8)
                    rollno=int(crl2)+1
                    print(rollno)
                    request.session['rollno']=rollno
                    d={'rollno':rollno,}
                    return render(request,"centerstudentregister.html",context=d)
            except:
                rollno=100001
                print("5"*8)
                request.session['rollno']=rollno
                d={'rollno':rollno,}
                print(rollno)
                return render(request,"centerstudentregister.html",context=d)
            print("6"*8)
            return render(request,"centerstudentregister.html")
    except:
        HttpResponse("You are not authorized!")

def create_centre_form(request):
    txtphoto = request.FILES['txtphoto']
    fs = FileSystemStorage()
    txtphotoprofile = fs.save(txtphoto.name,txtphoto)
    txtphotoprofile = fs.url(txtphotoprofile)

    centeruseriddefault=request.session['centeruser']
    nnkk=CentreRegisterAdmin.objects.get(center_id=centeruseriddefault)
    print("jjjjjjjjjjjjjjj",nnkk.center_name)

    crs=CentreRegisterStudent()
    crs.centeruserid=request.session['centeruser']
    crs.student_name=request.POST.get("txtstudentname","N/A")
    crs.mother_name=request.POST.get("txtmothername","N/A")
    crs.father_name=request.POST.get("txtfathername","N/A")
    crs.rollno=request.POST.get("txtrollno",0)
    crs.image=txtphotoprofile
    crs.Dob=request.POST.get("txtdob","N/A")

    crs.centre_name=nnkk.center_name
    crs.course_name=request.POST.get("txtcourse","N/A")
    crs.duration=request.POST.get("txtduration","n/a")
    crs.examheldon=request.POST.get("txtexam","N/A")
    crs.percent=request.POST.get("txtper",0)
    crs.grade=request.POST.get('txtgrade',"N/A")
    crs.session=request.POST.get("txtsession","N/A")
    crs.centre_code=request.session['centeruser']
    crs.dateofissue=request.POST.get("txtissue","N/A")
    crs.remark=request.POST.get("txtremark","N/A")
    crs.mark_s1=request.POST.get("txtmarks_sub1",0)
    crs.mark_s2=request.POST.get("txtmarks_sub2",0)
    crs.mark_s3=request.POST.get("txtmarks_sub3",0)
    crs.mark_s4=request.POST.get("txtmarks_sub4",0)
    crs.mark_s5=request.POST.get("txtmarks_sub5",0)
    crs.written_mark=request.POST.get("txtwritten_marks",0)
    crs.practical_mark=request.POST.get("txtprac_marks",0)
    crs.assignment_mark=request.POST.get("txtassignment_marks",0)
    crs.viva_mark=request.POST.get("txtviva_marks",0)
    crs.status="Reject"
    crs.studentdatetime=datetime.datetime.today()
    crs.save()
    messages.info(request,'Student register succussfully')
    return redirect('centerdashboard')


def adminstudentstatus(request):
    try:
        if request.session['adminid']:
            stdstall=CentreRegisterStudent.objects.all().order_by('-studentdatetime')
            return render(request,"adminstudentstatus.html",{'stdstall':stdstall})
        else:
            HttpResponse("You are not authorized!")

    except:
        HttpResponse("You are not authorized!")

def adminstudentactionaccept(request,id):
    try:
        if request.session['adminid']:
            hhj=CentreRegisterStudent.objects.get(rollno=id)
            hhj.status="Accept"
            hhj.save()
            print(id)
            messages.info(request,'Updated succussfully')
            return redirect('admindashboard')
    
    except ValueError:
        HttpResponse("You are not authorized!")


def adminstudentactionreject(request,id):
    try:
        if request.session['adminid']:
            hjhj=CentreRegisterStudent.objects.get(rollno=id)
            hjhj.status="Reject"
            hjhj.save()
            print(id)
            messages.info(request,'Updated succussfully')
            return redirect('admindashboard')
    
    except ValueError:
        HttpResponse("You are not authorized!")


def  admincentermanage(request):
    centmangreg=CentreRegisterAdmin.objects.all().order_by('-centerdatetime')
    return render(request,"admincentermanage.html",{'centmangreg':centmangreg})

def centeradminupdate(request):
    center_email=request.POST['center_email']
    center_mobile=request.POST['center_mobile']
    center_id=request.POST['center_id']
    center_name=request.POST['center_name'],
    center_address=request.POST['center_address'],
    center_password=request.POST['center_password'],
    adowner_name=request.POST['adowner_name'],
    # print(center_email,center_mobile,center_id,center_name,center_address)
    msg=''
    try:
    #msg=''
        ghh=CentreRegisterAdmin.objects.get(center_id=center_id)
        print(ghh)
        if ghh is not None:
                print("1"*8)
                ghh.center_name=center_name[0]
                ghh.center_address=center_address[0]
                ghh.center_mobile=center_mobile
                ghh.center_email=center_email
                ghh.center_password=center_password[0]
                ghh.owner_name=adowner_name[0]
                print("2"*8)
                ghh.save()
                messages.info(request,'Center Updated succussfully')
                return redirect('admindashboard')
        else:
            pass
    except:
        messages.info(request,'Bad request')
        return redirect('admindashboard')


def centerupdatestudent(request):
    centeruser=request.session['centeruser']
    # print(centersturollno)
    udsthnt=CentreRegisterStudent.objects.filter(centeruserid=centeruser).order_by('-studentdatetime')
    return render(request,"centerupdatestudent.html",{'udsthnt':udsthnt})

def studentcenterupdate(request):
    student_name=request.POST['student_name']
    mother_name=request.POST['mother_name']
    father_name=request.POST['father_name']
    session=request.POST['session']
    Dob=request.POST['Dob']
    stid=request.POST['stid']
    msg=''
    try:
    #msg=''
        if request.method == 'POST' and request.FILES['upload_result']:
            upload_result = request.FILES['upload_result']
            fs = FileSystemStorage()
            filenameprofile = fs.save(upload_result.name,upload_result)
            upload_result = fs.url(filenameprofile)
            nln=CentreRegisterStudent.objects.get(rollno=stid)
            print(nln)
            if nln is not None:
                    print("1"*8)
                    nln.student_name=student_name
                    nln.mother_name=mother_name
                    nln.father_name=father_name
                    nln.session=session
                    nln.Dob=Dob
                    nln.upload_result=upload_result
                    print("2"*8)
                    nln.save()
                    messages.info(request,'Student Updated succussfully')
                    return redirect('centerdashboard')



        
    except:
        dsfds=CentreRegisterStudent.objects.get(rollno=stid)
        print(dsfds)
        print("dsfds")
        if dsfds is not None:
                print("1"*8)
                dsfds.student_name=student_name
                dsfds.mother_name=mother_name
                dsfds.father_name=father_name
                dsfds.session=session
                dsfds.Dob=Dob
                print("2"*8)
                dsfds.save()
                messages.info(request,'Student Updated succussfully')
                return redirect('centerdashboard')
        else:
            pass
        messages.info(request,'Bad request')
        return redirect('centerdashboard')

def studentloginpage(request):
    return render(request,"studentloginpage.html")

def SearchStuRollnoe(request):
    searchrollno=request.POST['searchrollno']
    print(searchrollno)
    try:
        jbh=CentreRegisterStudent.objects.filter(rollno=searchrollno)
        if jbh is not None:
            print(jbh)
            print('1'*8)
            return render(request,"studentloginpage.html",{'jbh':jbh})
    except:
        print('2'*8)
        msg="Request not found"
        return render(request,"studentloginpage.html",{'msg':msg})


def Searchcenterid(request):
    searchcenterid=request.POST['searchcenterid']
    print(searchcenterid)
    try:
        hgg=CentreRegisterAdmin.objects.filter(center_id=searchcenterid)
        if hgg is not None:
            print(hgg)
            print('1'*8)
            # return render(request,"studentloginpage.html",{'jbhggh':hgg})
            return render(request,"search_center.html",{'Centerregister':hgg})

    except:
        print('2'*8)
        msg="Request not found"
        return render(request,"search_center.html",{'msg':msg})
        # return render(request,"studentloginpage.html",{'msg':msg})




def adminstudentsearch(request):
    adminsturollno=request.POST['adminsturollno']
    print(adminsturollno)
    try:
        gchghvhj=CentreRegisterStudent.objects.filter(rollno=adminsturollno)
        if gchghvhj is not None:
            print(gchghvhj)
            print('1'*8)
            return render(request,"adminstudentstatus.html",{'stdstall':gchghvhj})
    except:
        print('2'*8)
        msg="Request not found"
        return render(request,"adminstudentstatus.html",{'msg':msg})


def admincentersearch(request):
    admincenterid=request.POST['admincenterid']
    print(admincenterid)
    try:
        nnlnl=CentreRegisterAdmin.objects.filter(center_id=admincenterid)
        if nnlnl is not None:
            print(nnlnl)
            print('1'*8)
            return render(request,"admincentermanage.html",{'centmangreg':nnlnl})
    except:
        print('2'*8)
        msg="Request not found"
        return render(request,"admincentermanage.html",{'msg':msg})

def centerstudentsearch(request):
    centersturollno=request.POST['centersturollno']
    print(centersturollno)
    # request.session['centeruser']
    centeruser=request.session['centeruser']

    try:
        jkjk=CentreRegisterStudent.objects.filter(rollno=centersturollno,centeruserid=centeruser)
        if jkjk is not None:
            print(jkjk)
            print('1'*8)
            return render(request,"centerupdatestudent.html",{'udsthnt':jkjk})

    except:
        print('2'*8)
        msg="Request not found"
        return render(request,"centerupdatestudent.html",{'msg':msg})

######################################################################################
# def downloadresult(request):



from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter

def downloadresult(request,id):
    uihh=CentreRegisterStudent.objects.get(rollno=id)
    print("4"*8)
# photo='myineffable/img.jpg'
    Center_ID=uihh.centeruserid
    session=uihh.session
    W_m=uihh.written_mark
    P_m=uihh.practical_mark
    A_M=uihh.assignment_mark
    V_m=uihh.viva_mark
    Rollnumber=uihh.rollno

    photo=uihh.image
    photo=photo.split('/')
    photo=photo[1]+'/'+photo[2]
    print(photo)
    new_image_path=photo  #uihh.image

    name=uihh.student_name
    fname=uihh.father_name
    mname=uihh.mother_name
    dob=uihh.Dob
    Center_Name=uihh.centre_name
    Course_Name=uihh.course_name
    Duration=uihh.duration
    Exam_held_on=uihh.examheldon
    SUBJECT1=uihh.mark_s1
    SUBJECT2=uihh.mark_s2
    SUBJECT3=uihh.mark_s3
    SUBJECT4=uihh.mark_s4

    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4,letter
    from reportlab.lib.units import inch
    from reportlab.lib.utils import ImageReader
    from PyPDF2 import PdfReader
    from django.http import HttpResponse
    from reportlab.lib.pagesizes import letter
    # my_path='myineffable/MARKSHEET.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Marksheet.pdf"'
    c=canvas.Canvas(response,pagesize=A4)#letter
    c.translate(.2*inch,.2*inch) # set the starting point of coordinate margin
    c.setLineWidth(2)  #width of line
    c.setStrokeColorRGB(0,0,0)

    # #watermark with hadding
    c.rotate(45)
    c.setFillColorCMYK(0,0,0,0.08)  #color watermark
    c.setFont("Helvetica", 100)
    c.drawString(2*inch, 1*inch, "ineffableedu.in")
    c.rotate(-45)

    #watermark with Logo
    # c.rotate(45)
    # watermark = ImageReader('logo.png')
    # c.drawImage(watermark,2*inch,1*inch,700,50, mask='auto')
    # c.rotate(-45)


    # print('Check-1')

    c.line(0,0,7.8*inch,0) #x1,y1 x2,y2
    c.line(0,0,0,11.3*inch) #x1,y1 x2,y2
    c.line(0,11.3*inch,7.8*inch,11.3*inch) #x1,y1 x2,y2
    c.line(7.8*inch,11.3*inch,7.8*inch,0) #x1,y1 x2,y2
    c.setFillColor('BLACK')
    c.setFont("Helvetica",20) # font family and size#c.setFillColorCMYK(.2,.2,0,.39) # font colour as CMYK#c.setFillColorRGB(0,0,1) # font colour as RGB#c.setFillColor('lightgreen')#lawngreen, lightblue,lemonchiffonc.setFillColor('lightblue') #lavendarblushc.drawString(200,200,"Hello World") # write text in page
    # c.drawString(300,500,'Hi')  #width,heigh
    #logo path need
    logopic=r'myineffable/logo.jpeg'
    c.drawImage(logopic,0.1*inch,10.3*inch,width=100, height=70)
    #logo path need
    c.drawImage('myineffable/new_qr_code.jpeg',6.2*inch,10.3*inch,width=70, height=70)
    c.setFont("Helvetica-Bold",30)
    c.drawString(.2*inch,9.8*inch,'INEFFABLE GROUP OF INSTITUTION')
    c.setFont("Helvetica",10)
    c.drawString(2.2*inch,9.4*inch,'An institute registered under Trust act:- Reg No.26/23')
    c.drawString(2.9*inch,9.2*inch,'An ISO certified organization')
    # print('Check-2')
    c.setLineWidth(1)
    c.line(0.1*inch,9.1*inch,7.7*inch,9.1*inch) #x1,y1 x2,y2
    c.line(0.1*inch,7*inch,7.7*inch,7*inch) #x1,y1 x2,y2
    c.line(0.1*inch,9.1*inch,0.1*inch,7*inch) #x1,y1 x2,y2
    c.line(7.7*inch,7*inch,7.7*inch,9.1*inch) #x1,y1 x2,y2
    # print('Check-3')
    # c.setStrokeColorRGB(0,0,1)
    c.setFillColor('GREEN')
    c.setFont("Helvetica",20)
    c.drawString(2.9*inch,8.8*inch,'MARKSHEET')
    c.setFillColor('BLACK')
    c.setFont("Helvetica",10)
    # print('Check-4')
    c.drawString(0.4*inch,8.7*inch,'Name :')
    c.drawString(1.4*inch,8.7*inch,name)
    c.drawString(0.4*inch,8.5*inch,'Father Name :')
    c.drawString(1.4*inch,8.5*inch,fname)
    c.drawString(0.4*inch,8.3*inch,'Mother Name :')
    c.drawString(1.4*inch,8.3*inch,mname)
    c.drawString(0.4*inch,8.1*inch,'DOB :')
    c.drawString(1.4*inch,8.1*inch,dob)
    # print('Check-5')
    c.drawString(0.4*inch,7.9*inch,'Center Name :')
    c.drawString(1.4*inch,7.9*inch,Center_Name)
    c.drawString(0.4*inch,7.7*inch,'Course Name :')
    c.drawString(1.4*inch,7.7*inch,Course_Name)
    c.drawString(0.4*inch,7.5*inch,'Duration :')
    c.drawString(1.4*inch,7.5*inch,Duration)
    c.drawString(2.9*inch,7.2*inch,'Examination Held on :')
    c.drawString(4.3*inch,7.2*inch,Exam_held_on)
    # print('Check-6')
    c.drawString(5.6*inch,8.7*inch,'Roll No :')
    c.drawString(6.2*inch,8.7*inch,Rollnumber)
    # print('Check-7')
    c.drawImage(new_image_path,6*inch,7.2*inch,width=100, height=90)



    #course Modeule
    c.setLineWidth(1)
    c.line(0.1*inch,6.9*inch,7.7*inch,6.9*inch) #x1,y1 x2,y2
    c.line(0.1*inch,5*inch,7.7*inch,5*inch) #x1,y1 x2,y2
    c.line(0.1*inch,6.9*inch,0.1*inch,5*inch) #x1,y1 x2,y2
    c.line(7.7*inch,5*inch,7.7*inch,6.9*inch) #x1,y1 x2,y2
    c.setFillColor('GREEN')
    c.setFont("Helvetica",15)
    c.drawString(2.9*inch,6.7*inch,'COURSE MODULE')


    #subject
    c.setLineWidth(1)
    c.line(0.2*inch,6.6*inch,7.6*inch,6.6*inch) #x1,y1 x2,y2
    c.line(0.2*inch,5.1*inch,7.6*inch,5.1*inch) #x1,y1 x2,y2
    c.line(0.2*inch,6.6*inch,0.2*inch,5.1*inch) #x1,y1 x2,y2
    c.line(7.6*inch,5.1*inch,7.6*inch,6.6*inch) #x1,y1 x2,y2
    c.setFillColor('black')
    c.setFont("Helvetica",12)
    c.drawString(.5*inch,6.3*inch,'SUBJECT1 :-') #change
    c.drawString(1.6*inch,6.3*inch,SUBJECT1) #change
    c.drawString(.5*inch,6.0*inch,'SUBJECT2 :-') #change
    c.drawString(1.6*inch,6.0*inch,SUBJECT2) #change
    c.drawString(.5*inch,5.7*inch,'SUBJECT3 :-') #change
    c.drawString(1.6*inch,5.7*inch,SUBJECT3) #change
    c.drawString(.5*inch,5.4*inch,'SUBJECT4 :-') #change
    c.drawString(1.6*inch,5.4*inch,SUBJECT4) #change

    #Marksheet
    c.setLineWidth(1)  #width of line
    c.line(.8*inch,4.8*inch,7*inch,4.8*inch) #x1,y1 x2,y2
    c.line(.8*inch,4.6*inch,7*inch,4.6*inch) #x1,y1 x2,y2
    c.line(.8*inch,3*inch,7*inch,3*inch) #x1,y1 x2,y2
    c.line(.8*inch,4.8*inch,.8*inch,3*inch) #x1,y1 x2,y2

    c.line(7*inch,4.8*inch,7*inch,3*inch) #x1,y1 x2,y2
    c.line(2.6*inch,4.8*inch,2.6*inch,3*inch) #x1,y1 x2,y2
    c.line(4.1*inch,4.8*inch,4.1*inch,3*inch) #x1,y1 x2,y2
    c.line(5.6*inch,4.8*inch,5.6*inch,3*inch) #x1,y1 x2,y2

    c.setFillColor('black')
    c.setFont("Helvetica",10)
    c.drawString(1.1*inch,4.65*inch,'EXAM')
    c.drawString(2.9*inch,4.65*inch,'PASSING MARKS')
    c.drawString(4.3*inch,4.65*inch,'MARKS OBTAINED')
    c.drawString(5.9*inch,4.65*inch,'TOTAL MARKS')

    c.drawString(1.1*inch,4.3*inch,'WRITTEN')
    c.drawString(2.9*inch,4.3*inch,'35')
    c.drawString(4.3*inch,4.3*inch,W_m)
    c.drawString(5.9*inch,4.3*inch,'100')

    c.drawString(1.1*inch,4*inch,'PRACTICAL')
    c.drawString(2.9*inch,4*inch,'35')
    c.drawString(4.3*inch,4*inch,P_m)
    c.drawString(5.9*inch,4*inch,'100')


    c.drawString(.95*inch,3.7*inch,'ASSIGNMENT/PROJECT')
    c.drawString(2.9*inch,3.7*inch,'35')
    c.drawString(4.3*inch,3.7*inch,A_M)
    c.drawString(5.9*inch,3.7*inch,'100')

    c.drawString(1.1*inch,3.4*inch,'VIVA')
    c.drawString(2.9*inch,3.4*inch,'35')
    c.drawString(4.3*inch,3.4*inch,V_m)
    c.drawString(5.9*inch,3.4*inch,'100')


    #Scoreboard
    c.setLineWidth(1)  #width of line
    c.line(4*inch,2.7*inch,7.4*inch,2.7*inch) #x1,y1 x2,y2
    c.line(4*inch,1.4*inch,7.4*inch,1.4*inch) #x1,y1 x2,y2
    c.line(4*inch,2.35*inch,7.4*inch,2.35*inch) #x1,y1 x2,y2
    c.line(4*inch,2*inch,7.4*inch,2*inch) #x1,y1 x2,y2
    c.line(4*inch,1.7*inch,7.4*inch,1.7*inch) #x1,y1 x2,y2
    c.line(4*inch,2.7*inch,4*inch,1.4*inch) #x1,y1 x2,y2
    c.line(7.4*inch,2.7*inch,7.4*inch,1.4*inch) #x1,y1 x2,y2
    c.line(5.7*inch,2.7*inch,5.7*inch,1.4*inch) #x1,y1 x2,y2
    c.drawString(4.1*inch,2.5*inch,'PERCENTAGE')
    W_m1=int(W_m)
    P_m1=int(P_m)
    A_M1=int(A_M)
    V_m1=int(V_m)
    percent_var=((W_m1+P_m1+A_M1+V_m1)/400)*100
    percent_var = round(percent_var,1)
    percent_var1=str(percent_var)
    c.drawString(5.9*inch,2.5*inch,percent_var1)
    c.drawString(6.18*inch,2.5*inch,'%')

    c.drawString(4.1*inch,2.15*inch,'GRADE')
    if(percent_var>=75):
        grade='A+'
    elif(percent_var>=60):
        grade='A'
    elif(percent_var>=50):
        grade='B+'
    elif(percent_var>=35):
        grade='B'
    else:
        grade='F'
    c.drawString(5.9*inch,2.15*inch,grade)

    c.drawString(4.1*inch,1.82*inch,'SESSION')
    c.drawString(5.9*inch,1.82*inch,session)

    c.drawString(4.1*inch,1.5*inch,'CENTER CODE')
    c.drawString(5.9*inch,1.5*inch,str(Center_ID))
    #mohar path need
    c.drawImage('myineffable/mohar.jpeg',1.2*inch,1.7*inch,width=150, height=90)
    #manning_dirc path need
    c.drawImage('myineffable/manning_dirc.jpeg',0.6*inch,.6*inch,width=80, height=80)
    #manning_dirc path need
    c.drawImage('myineffable/exam_cont.jpeg',2.8*inch,.6*inch,width=80, height=80)





    #last
    c.line(.1*inch,.5*inch,7.7*inch,.5*inch) #x1,y1 x2,y2
    c.line(.1*inch,.09*inch,7.7*inch,.09*inch) #x1,y1 x2,y2
    c.line(.1*inch,.5*inch,.1*inch,.09*inch) #x1,y1 x2,y2
    c.line(7.7*inch,.5*inch,7.7*inch,.09*inch) #x1,y1 x2,y2
    c.setFont("Helvetica",10)
    c.drawString(1*inch,.3 *inch,'Registered Office- Laxmanpur , P.O- Surahi , Dist- Ballia , State- Uttar Pradesh, Pin code-277504')
    c.setFont("Helvetica",8)
    c.drawString(1.5*inch,.16*inch,'Helpline No. +91 7897993672 / website: www.ineffableedu.in / e-mail: ineffableedu@gmail.com')
    print("222222222222")
    c.showPage()
    import os
    print(os.getcwd())
    c.save()
    return response
    print("222222222222",c)

