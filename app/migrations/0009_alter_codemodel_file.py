# Generated by Django 4.0.2 on 2022-08-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_codemodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codemodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl elave edin'),
        ),
    ]
