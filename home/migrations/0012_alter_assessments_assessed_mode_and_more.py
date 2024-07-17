# Generated by Django 5.0.3 on 2024-07-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_banner_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessments',
            name='assessed_mode',
            field=models.CharField(blank=True, choices=[('Initial Phase', 'initial'), ('Processing Phase', 'processing'), ('Final Phase', 'final')], default='initial', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='assessments',
            name='assessment_for',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]