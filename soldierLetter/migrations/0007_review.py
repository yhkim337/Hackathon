# Generated by Django 4.0.6 on 2022-07-21 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soldierLetter', '0006_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
        ),
    ]