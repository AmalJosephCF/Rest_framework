# Generated by Django 5.0.2 on 2024-03-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='image/None/Noimg.jpg', upload_to='image/'),
        ),
    ]
