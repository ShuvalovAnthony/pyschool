# Generated by Django 3.2.4 on 2021-07-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_category_category_landing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_landing',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Лендинг курса'),
        ),
    ]
