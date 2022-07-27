# Generated by Django 4.0.6 on 2022-07-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneTable',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.IntegerField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'phone_table',
                'managed': False,
            },
        ),
    ]
