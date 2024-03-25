# Generated by Django 5.0.3 on 2024-03-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0006_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arms_Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='gallery')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]