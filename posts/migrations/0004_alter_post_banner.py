# Generated by Django 5.1.6 on 2025-03-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='Capture3.png', upload_to=''),
        ),
    ]
