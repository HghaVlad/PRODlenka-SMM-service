# Generated by Django 4.2.11 on 2024-04-02 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspace', '0001_initial'),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.workspace'),
        ),
    ]
