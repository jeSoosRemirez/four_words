# Generated by Django 2.0.7 on 2018-07-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_words', '0003_oneword'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourwords',
            name='adjective_desription',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='adjective_example',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='adjective_translate',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='adverb_desription',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='adverb_example',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='adverb_translate',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='noun_desription',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='noun_example',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='noun_translate',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='verb_desription',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='verb_example',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='fourwords',
            name='verb_translate',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
