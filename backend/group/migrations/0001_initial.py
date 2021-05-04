# Generated by Django 3.0.5 on 2021-05-03 23:51

from django.db import migrations, models
import djongo.models.fields
import group.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fed_times', djongo.models.fields.ArrayField(model_container=group.models.Fed, model_form_class=group.models.FedForm)),
                ('group_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['group_code'], name='group_group_group_c_4481b5_idx'),
        ),
    ]
