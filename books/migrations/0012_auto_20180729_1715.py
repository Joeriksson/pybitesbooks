# Generated by Django 2.0.7 on 2018-07-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20180729_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknote',
            name='type_note',
            field=models.CharField(choices=[('q', 'Quote'), ('n', 'Note')], default='n', max_length=1),
        ),
    ]