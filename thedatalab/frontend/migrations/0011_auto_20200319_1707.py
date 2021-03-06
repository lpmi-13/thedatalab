# Generated by Django 2.2.6 on 2020-03-19 17:07

from django.db import migrations, models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_auto_20200319_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='redirect_to',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, force_lowercase=True, help_text='eg: blog-post, podcast', initial='blog-post, podcast', to='frontend.Types'),
        ),
        migrations.AlterField(
            model_name='page',
            name='colour_scheme',
            field=models.CharField(blank=True, choices=[['', ''], ['green', 'Green'], ['orange', 'Orange'], ['blue', 'Blue'], ['red', 'Red']], max_length=150),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_type',
            field=models.CharField(blank=True, choices=[['', 'Static page'], ['papers', 'Papers'], ['blog', 'Blog'], ['topic', 'Topic']], max_length=150),
        ),
    ]
