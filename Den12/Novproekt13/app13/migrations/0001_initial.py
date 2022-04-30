# Generated by Django 4.0.4 on 2022-04-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zemji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, unique=True)),
                ('population', models.IntegerField()),
                ('year_change', models.FloatField()),
                ('net_change', models.IntegerField()),
                ('density', models.IntegerField()),
                ('land_area', models.IntegerField()),
                ('med_age', models.IntegerField()),
                ('urban_pop', models.IntegerField()),
                ('world_share', models.FloatField()),
            ],
        ),
    ]