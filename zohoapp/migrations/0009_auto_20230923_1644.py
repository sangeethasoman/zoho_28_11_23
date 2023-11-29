# Generated by Django 3.2.20 on 2023-09-23 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0008_auto_20230923_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='expense',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='expense',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='activation_tag',
            field=models.CharField(default='', max_length=255),
        ),
    ]