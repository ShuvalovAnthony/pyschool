# Generated by Django 3.2.4 on 2021-07-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_category_category_landing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='klass',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
