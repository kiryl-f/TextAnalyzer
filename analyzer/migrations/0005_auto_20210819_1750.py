# Generated by Django 3.2.5 on 2021-08-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0004_auto_20210809_1805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['title', 'text'], 'verbose_name': 'Текст', 'verbose_name_plural': 'Текст'},
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
