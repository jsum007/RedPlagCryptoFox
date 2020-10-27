# Generated by Django 3.1.2 on 2020-10-27 11:59

from django.db import migrations, models
import rest.app.fileUpDown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.UUIDField(default=None)),
                ('file', models.FileField(upload_to=rest.app.fileUpDown.models.upload_path)),
            ],
        ),
    ]
