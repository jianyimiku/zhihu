# Generated by Django 2.2.6 on 2020-02-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='标题'),
        ),
    ]
