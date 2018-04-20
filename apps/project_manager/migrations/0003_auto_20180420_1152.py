# Generated by Django 2.0.2 on 2018-04-20 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0002_auto_20180420_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('file_name', models.CharField(default='', max_length=256, verbose_name='文件名')),
                ('file_size', models.IntegerField(default=0, verbose_name='文件大小，单位B')),
                ('files', models.FileField(upload_to='files/%Y/%m/%d/')),
                ('encryption_key', models.CharField(default='', max_length=128, verbose_name='加密秘钥')),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件',
                'db_table': 'sqlaudit_files',
                'default_permissions': (),
            },
        ),
        migrations.RemoveField(
            model_name='oldataexportdetail',
            name='encryption_key',
        ),
        migrations.RemoveField(
            model_name='oldataexportdetail',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='oldataexportdetail',
            name='file_size',
        ),
        migrations.RemoveField(
            model_name='oldataexportdetail',
            name='files',
        ),
        migrations.AddField(
            model_name='files',
            name='export',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manager.OlDataExportDetail', verbose_name='管理导出文件id'),
        ),
    ]