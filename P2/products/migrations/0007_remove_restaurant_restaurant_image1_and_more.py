# Generated by Django 4.0.3 on 2022-03-12 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurant_image1',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurant_image2',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurant_image3',
        ),
        migrations.CreateModel(
            name='Restaurant_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='restaurant_images/')),
                ('belong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.restaurant')),
            ],
        ),
    ]
