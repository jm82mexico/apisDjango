# Generated by Django 4.1.2 on 2022-10-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
