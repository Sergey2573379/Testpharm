# Generated by Django 4.2.16 on 2024-11-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('editdate', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
        ),
    ]
