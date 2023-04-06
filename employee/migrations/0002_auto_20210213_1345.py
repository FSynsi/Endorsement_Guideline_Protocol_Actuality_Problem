# Generated by Django 2.0.5 on 2021-02-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_reg',
            old_name='name',
            new_name='fname',
        ),
        migrations.RemoveField(
            model_name='employee_reg',
            name='address',
        ),
        migrations.AddField(
            model_name='employee_reg',
            name='gender',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_reg',
            name='lname',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_reg',
            name='uname',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
