# Generated by Django 3.2.4 on 2021-06-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humaniser2', '0002_auto_20210626_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_month',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='street',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
