# Generated by Django 4.0.2 on 2022-08-09 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_codemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codemodel',
            old_name='Code',
            new_name='code',
        ),
        migrations.AddField(
            model_name='codemodel',
            name='coder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazıçı'),
        ),
        migrations.AlterField(
            model_name='codemodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fayl elave edin'),
        ),
    ]
