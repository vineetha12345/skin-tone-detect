# Generated by Django 3.2.2 on 2021-05-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_tone', '0002_rename_upload_img_skintone_formfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skintone',
            name='formfile',
            field=models.ImageField(blank=True, upload_to='input'),
        ),
    ]
