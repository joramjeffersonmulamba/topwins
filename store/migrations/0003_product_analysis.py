# Generated by Django 5.0.6 on 2024-06-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='analysis',
            field=models.TextField(default='No analysis available yet.', max_length=20),
        ),
    ]