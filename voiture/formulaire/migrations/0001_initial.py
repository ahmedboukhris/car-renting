# Generated by Django 4.1.4 on 2023-01-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prénom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mot_de_passe', models.CharField(max_length=200)),
            ],
        ),
    ]
