# Generated by Django 3.2.11 on 2022-02-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aligner', '0005_auto_20220201_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frenchword',
            old_name='sent_aligned',
            new_name='en_sent_aligned',
        ),
        migrations.RenameField(
            model_name='frenchword',
            old_name='sent_id',
            new_name='en_sent_id',
        ),
        migrations.AddField(
            model_name='frenchword',
            name='la_sent_aligned',
            field=models.CharField(blank=True, default='None Provided', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='frenchword',
            name='la_sent_id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
