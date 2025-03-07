# Generated by Django 5.1.1 on 2024-09-20 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('rooms_type', models.CharField(choices=[('single_room', 'single_room'), ('double_room', 'double_room'), ('suite', 'suite'), ('family_room', 'family_room')], max_length=255)),
                ('check_date', models.DateField(auto_now_add=True)),
                ('checkout_date', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('request', models.CharField(max_length=225)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.room')),
            ],
            options={
                'verbose_name': 'detail',
                'verbose_name_plural': 'details',
                'db_table': 'detail',
                'ordering': ['-id'],
            },
        ),
    ]
