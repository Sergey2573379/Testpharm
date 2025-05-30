# Generated by Django 4.2.16 on 2024-12-23 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_caetegory_dorixona_drug_caetegorydorixona_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentdrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=2000, verbose_name='Текст')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('editdate', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('comusers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users')),
            ],
        ),
    ]
