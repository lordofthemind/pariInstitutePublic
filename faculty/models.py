from django.db import models
import uuid

# Create your models here.
class Faculty(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    mobile = models.CharField(max_length=15,unique=True)
    email = models.CharField(max_length=254,unique=True)
    password = models.CharField(max_length=50)
    dob = models.DateField(blank=True,null=True)
    pic = models.FileField(upload_to='Imgs/Faculty',blank=True,null=True)
    qualification = models.CharField(max_length=50,null=True,blank=True)
    qualf_pic = models.FileField(upload_to='Docs/Faculty',blank=True,null=True)
    experties_1 = models.CharField(max_length=20,blank=True,null=True)
    experties_2 = models.CharField(max_length=20,blank=True,null=True)
    doc_type = models.CharField(max_length=20)
    doc_num = models.CharField(max_length=20)
    doc_pic = models.FileField(upload_to='Docs/Faculty',blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.fname+' '+self.lname+' '+self.qualification