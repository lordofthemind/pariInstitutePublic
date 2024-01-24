# Generated by Django 4.0.4 on 2022-07-16 16:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=70)),
                ('lname', models.CharField(max_length=70)),
                ('fathers_nm', models.CharField(blank=True, max_length=70, null=True)),
                ('mothers_nm', models.CharField(blank=True, max_length=70, null=True)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('pic', models.FileField(blank=True, null=True, upload_to='Imgs/Student')),
                ('qualification', models.CharField(blank=True, max_length=50, null=True)),
                ('mrksht_10th', models.FileField(upload_to='Docs/Student')),
                ('mrksht_12th', models.FileField(blank=True, null=True, upload_to='Docs/Student')),
                ('doc_type', models.CharField(max_length=20)),
                ('doc_num', models.CharField(max_length=20)),
                ('doc_pic', models.FileField(upload_to='Docs/Student')),
                ('sign_pic', models.FileField(blank=True, null=True, upload_to='Docs/Student')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='Docs/Student')),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
