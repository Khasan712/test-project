# Generated by Django 4.2.3 on 2023-08-01 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='kurs',
            field=models.CharField(choices=[('backend', 'backend'), ('frontend', 'frontend'), ('mobile', 'mobile')], max_length=8),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
