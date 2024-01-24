from django.db import models
from student.models import Student
from faculty.models import Faculty
import uuid


# Create your models here.
class Superuser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13, unique=True)
    email = models.CharField(max_length=254, unique=True)
    dob = models.DateField(blank=True, null=True)
    pic = models.FileField(upload_to="Imgs/Superuser", blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    designation = models.CharField(max_length=70, blank=True, null=True)
    occupation = models.CharField(max_length=70, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=75, unique=True)
    fee = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, null=True
    )  # add decimalfield
    pic = models.FileField(upload_to="Imgs/Superuser", blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    lectures = models.CharField(max_length=20, blank=True, null=True)
    categories = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)
    srt_desc = models.CharField(max_length=100)
    lng_desc = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name + " " + self.duration


class CrsLrn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lrn_nm = models.TextField(null=True, blank=True)
    lrn_dsc = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.lrn_nm + " " + self.course.name


class Batch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timing = models.TimeField()
    start_dt = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.course.name + " " + str(self.start_dt) + " " + str(self.timing)
