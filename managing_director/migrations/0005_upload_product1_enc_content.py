# Generated by Django 2.0.5 on 2021-02-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing_director', '0004_auto_20210216_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_product1',
            name='enc_content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
