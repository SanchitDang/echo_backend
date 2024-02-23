# Generated by Django 5.0.1 on 2024-02-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0018_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scraps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('user_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('user_id', models.CharField(max_length=10)),
            ],
        ),
    ]
