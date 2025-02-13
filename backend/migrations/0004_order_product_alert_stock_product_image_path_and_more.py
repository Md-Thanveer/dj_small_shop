# Generated by Django 5.1.5 on 2025-02-06 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_brand_image_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=255)),
                ('payment_method', models.CharField(choices=[('CASH', 'CASH'), ('UPI', 'UPI'), ('CARD', 'CARD')], default='CASH', max_length=255)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='alert_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_path',
            field=models.ImageField(blank=True, default='no-image-available.jpg', null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image_path',
            field=models.ImageField(blank=True, default='No_image_available.jpg', null=True, upload_to='brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(default=0)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.product')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
    ]
