# Generated by Django 3.2.2 on 2021-05-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_tone', '0003_alter_skintone_formfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skintone',
            name='formfile',
            field=models.ImageField(upload_to='', verbose_name='blank=True'),
        ),
    ]
