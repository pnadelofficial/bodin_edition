# Generated by Django 3.2.11 on 2022-02-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aligner', '0007_auto_20220221_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='englishword',
            name='unaligned_id',
            field=models.CharField(blank=True, default='None Provided', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='frenchword',
            name='unaligned_id',
            field=models.CharField(blank=True, default='None Provided', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='latinword',
            name='unaligned_id',
            field=models.CharField(blank=True, default='None Provided', max_length=30, null=True),
        ),
    ]