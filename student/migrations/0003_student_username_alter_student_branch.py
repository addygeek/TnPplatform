# Generated by Django 5.0.2 on 2024-02-17 05:47

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_student_roll_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='uname', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='Branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE')], max_length=50),
        ),
    ]
