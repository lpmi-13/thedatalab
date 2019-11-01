# Generated by Django 2.2.6 on 2019-11-01 07:56

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20180615_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('menu_title', models.CharField(blank=True, max_length=150)),
                ('show_in_menu', models.BooleanField(default=False)),
                ('meta_title', models.CharField(blank=True, max_length=150)),
                ('body', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='frontend.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
