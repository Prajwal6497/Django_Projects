# Generated by Django 4.2.2 on 2023-07-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stucomment',
            field=models.CharField(default='not available', max_length=50),
        ),
    ]
