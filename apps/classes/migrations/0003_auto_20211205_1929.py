# Generated by Django 3.2.5 on 2021-12-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('home', '0015_alter_profil_image'),
        ('classes', '0002_alter_classlevels_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlist',
            name='teacher',
            field=models.ManyToManyField(blank=True, to='home.Profil', verbose_name='Sınıf Öğretmeni'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='students',
            field=models.ManyToManyField(blank=True, to='student.Student'),
        ),
    ]
