# Generated by Django 4.1.7 on 2023-03-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_product_type_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('ts', 'Футболка'), ('sh', 'Шеврон'), ('t', 'Толстовка'), ('ot', 'Остальное')], default=('ot', 'Остальное'), max_length=200),
        ),
    ]
