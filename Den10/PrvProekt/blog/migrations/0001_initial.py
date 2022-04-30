# Generated by Django 4.0.4 on 2022-04-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=50)),
                ('grad', models.CharField(max_length=50)),
                ('adresa', models.CharField(max_length=50)),
                ('dataRagjanje', models.DateField()),
                ('telefonskibroj', models.CharField(max_length=50)),
                ('clenski_broj', models.IntegerField()),
                ('dataClenstvo', models.DateField()),
                ('pozajmenoKniga', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Knigi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=50, unique=True)),
                ('avtor', models.CharField(max_length=50)),
                ('zanr', models.CharField(max_length=50)),
                ('kolicina', models.IntegerField()),
                ('GodinaIzdavanje', models.IntegerField()),
            ],
        ),
    ]