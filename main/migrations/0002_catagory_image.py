# Generated by Django 2.1.1 on 2018-09-04 07:35

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path),
        ),
    ]