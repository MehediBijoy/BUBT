# Generated by Django 3.1.7 on 2021-03-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='url',
            field=models.URLField(default='https://meet.google.com/', max_length=300),
        ),
    ]