# Generated by Django 3.2.4 on 2021-07-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210706_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_lesson_bots',
            field=models.CharField(default='nastrojka-bota', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_lesson_ege',
            field=models.CharField(default='testovyj-ege', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_lesson_python',
            field=models.CharField(default='tipy-dannyh', max_length=50),
        ),
    ]