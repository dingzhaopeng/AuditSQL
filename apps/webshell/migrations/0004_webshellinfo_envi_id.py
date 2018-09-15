# Generated by Django 2.1.1 on 2018-09-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshell', '0003_remove_webshellinfo_envi'),
    ]

    operations = [
        migrations.AddField(
            model_name='webshellinfo',
            name='envi_id',
            field=models.IntegerField(choices=[(1, '生产环境'), (2, '测试环境')], default=0, verbose_name='环境'),
            preserve_default=False,
        ),
    ]