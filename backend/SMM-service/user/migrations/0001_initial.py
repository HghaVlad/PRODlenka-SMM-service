# Generated by Django 4.2.11 on 2024-04-02 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('telegram_id', models.BigIntegerField(unique=True)),
                ('telegram_username', models.CharField(max_length=32)),
                ('avatar', models.CharField(default=None, null=True)),
                ('last_logged_in', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
