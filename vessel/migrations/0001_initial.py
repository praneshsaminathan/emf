# Generated by Django 2.1.5 on 2019-01-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VesselInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('mode', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive'), ('T', 'Trash')], default='A', max_length=1)),
                ('speed', models.IntegerField(blank=True, help_text='The speed (in knots x10) that the subject vessel is reporting according to AIS transmissions', null=True, verbose_name='Speed')),
                ('ship_name', models.CharField(blank=True, help_text='The Shipname of the subject vessel', max_length=150, null=True, verbose_name='Ship Name')),
                ('ship_type', models.IntegerField(blank=True, help_text='The Shiptype of the subject vessel according to AIS transmissions', null=True, verbose_name='Ship Type')),
                ('type_name', models.CharField(blank=True, help_text='The Type of the subject vessel', max_length=150, null=True, verbose_name='Type Name')),
                ('imo', models.BigIntegerField(help_text='International Maritime Organisation number - seven-digit number that uniquely identifies vessels', unique=True, verbose_name='IMO')),
                ('length', models.FloatField(blank=True, help_text='The overall Length (in metres) of the subject vessel', null=True, verbose_name='Length')),
                ('width', models.FloatField(blank=True, help_text='The Breadth (in metres) of the subject vessel', null=True, verbose_name='Width')),
                ('year_built', models.IntegerField(blank=True, help_text='The year that the subject vessel was built', null=True, verbose_name='Year Built')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
