# Generated by Django 4.0.6 on 2022-07-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soldierLetter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encourage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=30)),
            ],
        ),
    ]
