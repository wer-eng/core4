# Generated by Django 3.2.5 on 2021-12-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_profil_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='image',
            field=models.ImageField(default='images/person.png', upload_to='images/ogretmenler/'),
        ),
    ]
