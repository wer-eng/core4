# Generated by Django 3.2.5 on 2021-12-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_delete_studentlist'),
        ('home', '0015_alter_profil_image'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.session')),
                ('students', models.ManyToManyField(blank=True, to='student.Student')),
                ('teacher', models.ManyToManyField(blank=True, to='home.Profil', verbose_name='Sınıf Öğretmeni')),
            ],
        ),
    ]
