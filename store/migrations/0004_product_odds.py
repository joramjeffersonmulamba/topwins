# Generated by Django 5.0.6 on 2024-06-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_analysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='odds',
            field=models.ImageField(default='No analysis available yet.', max_length=4, upload_to=''),
        ),
    ]
