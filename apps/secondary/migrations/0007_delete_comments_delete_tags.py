# Generated by Django 5.0.3 on 2024-03-21 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0006_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
