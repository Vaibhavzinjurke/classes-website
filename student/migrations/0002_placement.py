# Generated by Django 5.0.2 on 2024-03-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
            ],
        ),
    ]
