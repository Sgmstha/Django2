# Generated by Django 5.0.4 on 2024-04-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
