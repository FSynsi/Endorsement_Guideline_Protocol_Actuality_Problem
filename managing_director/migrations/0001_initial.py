# Generated by Django 2.0.5 on 2021-01-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload_product1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=300)),
                ('send_to', models.CharField(max_length=200)),
                ('work_requirements', models.FileField(upload_to='')),
                ('file_path', models.CharField(max_length=300)),
            ],
        ),
    ]
