# Generated by Django 3.0.3 on 2020-03-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products_images/def.jpg', upload_to='products_images/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
