# Generated by Django 3.1.5 on 2021-01-21 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Programs', '0002_intake'),
        ('Classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='intake',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Programs.intake'),
            preserve_default=False,
        ),
    ]
