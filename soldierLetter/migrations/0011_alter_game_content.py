# Generated by Django 4.0.6 on 2022-07-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soldierLetter', '0010_alter_game_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
