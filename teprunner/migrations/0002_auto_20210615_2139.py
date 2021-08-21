# Generated by Django 3.1.3 on 2021-06-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teprunner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='filename',
            field=models.CharField(default='', max_length=200, verbose_name='文件名'),
        ),
        migrations.AddField(
            model_name='case',
            name='source',
            field=models.CharField(default='platform', max_length=10, verbose_name='用例来源'),
        ),
        migrations.AddField(
            model_name='project',
            name='git_branch',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Git分支'),
        ),
        migrations.AddField(
            model_name='project',
            name='git_repository',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Git仓库'),
        ),
        migrations.AddField(
            model_name='project',
            name='last_sync_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='运行时间'),
        ),
    ]