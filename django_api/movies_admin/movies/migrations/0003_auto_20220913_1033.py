# Generated by Django 3.2 on 2022-09-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220912_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Персона', 'verbose_name_plural': 'Персоны'},
        ),
        migrations.AlterModelOptions(
            name='personfilmwork',
            options={'verbose_name': 'Персона', 'verbose_name_plural': 'Персоны'},
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='certificate',
            field=models.CharField(max_length=512, null=True, verbose_name='certificate'),
        ),
    ]