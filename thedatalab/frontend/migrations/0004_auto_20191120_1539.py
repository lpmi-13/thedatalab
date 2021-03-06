# Generated by Django 2.2.6 on 2019-11-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20191120_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Author'),
        ),
        migrations.AlterField(
            model_name='project',
            name='overlay_url',
            field=models.URLField(blank=True),
        ),
    ]
