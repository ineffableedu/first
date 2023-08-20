from django.db import models

# Create your models here.



class CentreRegisterAdmin(models.Model):
     center_id=models.CharField(max_length=500,primary_key = True)
     center_name=models.CharField(max_length=500, null = True , blank = True)
     center_photo=models.CharField(max_length=500, null = True , blank = True)
     center_address=models.CharField(max_length=500, null = True , blank = True)
     center_mobile=models.CharField(max_length=500, null = True , blank = True)
     center_email=models.CharField(max_length=500, null = True , blank = True)
     centerdatetime=models.CharField(max_length=500, null = True , blank = True)
     center_password=models.CharField(max_length=500, null = True , blank = True)
     owner_name=models.CharField(max_length=500, null = True , blank = True)



class CentreRegisterStudent(models.Model):
     student_name=models.CharField(max_length=255)
     mother_name=models.CharField(max_length=255)
     father_name=models.CharField(max_length=255)
     rollno=models.CharField(max_length=255,primary_key = True)
     image=models.CharField(max_length=255)
     Dob=models.CharField(max_length=255)
     centre_name=models.CharField(max_length=255)
     course_name=models.CharField(max_length=255)
     duration=models.CharField(max_length=255)
     examheldon=models.CharField(max_length=255)
     percent=models.CharField(max_length=255)
     grade=models.CharField(max_length=255)
     session=models.CharField(max_length=255)
     centre_code=models.CharField(max_length=255)
     dateofissue=models.CharField(max_length=255)
     remark=models.CharField(max_length=255)
     mark_s1=models.CharField(max_length=255)
     mark_s2=models.CharField(max_length=255)
     mark_s3=models.CharField(max_length=255)
     mark_s4=models.CharField(max_length=255)
     mark_s5=models.CharField(max_length=255)
     written_mark=models.CharField(max_length=255)
     practical_mark=models.CharField(max_length=255)
     assignment_mark=models.CharField(max_length=255)
     viva_mark=models.CharField(max_length=255)
     centeruserid=models.CharField(max_length=255)
     status=models.CharField(max_length=255)
     upload_result=models.CharField(max_length=255,null=True,blank=True)
     studentdatetime=models.CharField(max_length=500, null = True , blank = True)

