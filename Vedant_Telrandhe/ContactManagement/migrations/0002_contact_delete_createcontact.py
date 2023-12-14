# Generated by Django 5.0 on 2023-12-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, unique=True)),
                ('emailId', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CreateContact',
        ),
    ]
