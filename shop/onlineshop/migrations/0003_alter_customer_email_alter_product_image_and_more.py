# Generated by Django 4.0.4 on 2022-05-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static\\images\\default-product-img.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
