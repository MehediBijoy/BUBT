# Generated by Django 3.1.7 on 2021-03-12 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Programs', '0001_initial'),
        ('Users', '0001_initial'),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=10, unique=True)),
                ('class_name', models.CharField(max_length=50, unique=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
                ('course_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_teacher', to='Users.teacher')),
                ('intake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Programs.intake')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Programs.program')),
                ('students', models.ManyToManyField(blank=True, related_name='students', to='Users.student')),
            ],
        ),
    ]
