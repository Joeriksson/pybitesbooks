# Generated by Django 2.0.7 on 2018-10-03 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_booknote_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbook',
            options={'ordering': ['-completed', '-id']},
        ),
    ]
