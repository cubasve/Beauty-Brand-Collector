# Generated by Django 3.0.7 on 2020-07-04 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200704_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-date']},
        ),
    ]
