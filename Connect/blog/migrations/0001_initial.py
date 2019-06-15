# Generated by Django 2.2.1 on 2019-06-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
