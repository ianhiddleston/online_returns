# Generated by Django 2.1.3 on 2019-02-18 20:58

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0004_auto_20181125_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guildrank',
            options={'ordering': ['guild__name', 'social_standing', 'rank']},
        ),
        migrations.AddField(
            model_name='character',
            name='ended',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guild',
            name='banned_races',
            field=models.ManyToManyField(to='character.Race'),
        ),
        migrations.AddField(
            model_name='guildrank',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guildrank',
            name='tithe_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guildrank',
            name='tithe_percent',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='player',
            name='registered',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='character',
            name='started',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='player',
            name='next_kin_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number should be entered in the format: '+xx9999999'. UK numbers are +44 and drop leading '0'. For example +441632962499. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='player',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number should be entered in the format: '+xx9999999'. UK numbers are +44 and drop leading '0'. For example +441632962499. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]