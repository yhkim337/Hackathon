# Generated by Django 4.0.6 on 2022-07-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_sub_type_profile_sub_type1_profile_sub_type2'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stock_type',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
