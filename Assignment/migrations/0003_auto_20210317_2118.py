# Generated by Django 3.1.7 on 2021-03-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0002_assignment_participants_file_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment_participants',
            name='student_name',
        ),
        migrations.AddField(
            model_name='assignment_participants',
            name='student_id',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
