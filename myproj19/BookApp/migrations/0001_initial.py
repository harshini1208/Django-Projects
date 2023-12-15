# Generated by Django 4.2.7 on 2023-12-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=30)),
                ('published_year', models.DateField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
