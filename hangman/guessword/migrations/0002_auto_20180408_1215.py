# Generated by Django 2.0.4 on 2018-04-08 08:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('guessword', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='wordsmodel',
            managers=[
                ('words', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='wordsmodel',
            name='word',
            field=models.CharField(help_text='Words which need to be guessed', max_length=128),
        ),
    ]