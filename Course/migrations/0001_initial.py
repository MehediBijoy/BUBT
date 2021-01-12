# Generated by Django 3.1 on 2020-08-22 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10, unique=True)),
                ('course_title', models.CharField(max_length=100)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Programs.program')),
            ],
        ),
    ]
