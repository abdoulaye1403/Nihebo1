# Generated by Django 3.2.6 on 2021-09-13 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hebogoundo', '0006_auto_20210912_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hebogoundo.category'),
            preserve_default=False,
        ),
    ]
