# Generated by Django 5.1.4 on 2024-12-30 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('phone', 'phone'), ('laptop', 'laptop'), ('accessories', 'accessories')], max_length=100, null=True),
        ),
    ]