# Generated by Django 3.2.11 on 2022-01-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(default='None Provided', max_length=30)),
                ('word_id', models.IntegerField()),
                ('sent_id', models.IntegerField()),
                ('lemma', models.CharField(blank=True, default='None Provided', max_length=30, null=True)),
                ('PartOfSpeech', models.CharField(blank=True, default='None Provided', max_length=30, null=True)),
                ('UDRelation', models.CharField(blank=True, default='None Provided', max_length=30, null=True)),
                ('features', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TargetWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(default='None Provided', max_length=30)),
                ('word_id', models.IntegerField()),
                ('sent_id', models.IntegerField()),
                ('align_id', models.CharField(default='None Provided', max_length=30)),
                ('lemma', models.CharField(blank=True, default='None Provided', max_length=30, null=True)),
                ('PartOfSpeech', models.CharField(blank=True, default='None Provided', max_length=30, null=True)),
                ('UDRelation', models.CharField(blank=True, default='None Provided', max_length=30, null=True)),
                ('features', models.CharField(blank=True, default='None Provided', max_length=30, null=True)),
            ],
        ),
    ]
