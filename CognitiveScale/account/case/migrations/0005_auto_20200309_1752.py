# Generated by Django 2.1.7 on 2020-03-09 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_auto_20200309_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.Account'),
        ),
    ]
