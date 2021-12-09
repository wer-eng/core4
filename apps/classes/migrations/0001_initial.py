# Generated by Django 3.2.5 on 2021-12-04 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0015_alter_profil_image'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ClassLevels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='9', max_length=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='A', max_length=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.session')),
                ('students', models.ManyToManyField(to='student.Student')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='className',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='classes.classnames'),
        ),
        migrations.AddField(
            model_name='classes',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classlevels'),
        ),
    ]
