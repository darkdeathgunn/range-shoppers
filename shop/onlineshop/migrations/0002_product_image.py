# Generated by Django 4.0.4 on 2022-05-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static\\images\\default-product-img.png', upload_to='static\\images'),
        ),
    ]
