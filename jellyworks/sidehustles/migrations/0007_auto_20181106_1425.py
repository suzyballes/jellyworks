# Generated by Django 2.1.3 on 2018-11-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidehustles', '0006_auto_20181106_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]