# Generated by Django 4.2.1 on 2023-06-17 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rezervace', '0002_zakaznik_profilovyobrazek_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rezervace',
            name='jmenoZakaznika',
        ),
        migrations.RemoveField(
            model_name='rezervace',
            name='prijmeniZakaznika',
        ),
        migrations.AddField(
            model_name='rezervace',
            name='pokoj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rezervace.pokoj', verbose_name='Pokoj'),
        ),
        migrations.AddField(
            model_name='rezervace',
            name='zakaznik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rezervace.zakaznik', verbose_name='Zákazník'),
        ),
    ]