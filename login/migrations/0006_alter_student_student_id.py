# Generated by Django 5.1.1 on 2024-10-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0005_remove_subject_students_student_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.IntegerField(unique=True),
        ),
    ]
