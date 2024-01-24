from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    fathers_nm = models.CharField(max_length=70,blank=True,null=True)
    mothers_nm = models.CharField(max_length=70,blank=True,null=True)
    mobile = models.CharField(max_length=15,unique=True)
    email = models.CharField(max_length=254,unique=True)
    password = models.CharField(max_length=50)
    dob = models.DateField(blank=True,null=True)
    pic = models.FileField(upload_to='Imgs/Student',null=True,blank=True)
    qualification = models.CharField(max_length=50,null=True,blank=True)
    mrksht_10th = models.FileField(upload_to='Docs/Student')
    mrksht_12th = models.FileField(upload_to='Docs/Student',blank=True,null=True)
    doc_type = models.CharField(max_length=20)
    doc_num = models.CharField(max_length=20)
    doc_pic = models.FileField(upload_to='Docs/Student')
    sign_pic = models.FileField(upload_to='Docs/Student',blank=True,null=True)
    certificate = models.FileField(upload_to='Docs/Student',blank=True,null=True)
    address = models.CharField(max_length=120,blank=True,null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True)
    # for_corse = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.fname+' '+self.lname+' '+self.doc_num


