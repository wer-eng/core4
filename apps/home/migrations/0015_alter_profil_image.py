# Generated by Django 3.2.5 on 2021-12-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_profil_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='image',
            field=models.ImageField(blank=True, default='images/person.png', null=True, upload_to='images/ogretmenler/'),
        ),
    ]
