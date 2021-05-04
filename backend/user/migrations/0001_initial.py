# Generated by Django 3.0.5 on 2021-05-03 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('firebase_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('groups', models.ManyToManyField(to='group.Group')),
            ],
        ),
    ]
