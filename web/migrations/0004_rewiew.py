# Generated by Django 5.1.1 on 2024-09-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_request_detail_request_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewiew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('short_discription', models.CharField(max_length=225)),
                ('rating', models.FloatField(choices=[('single_room', 'single_room'), ('double_room', 'double_room'), ('suite', 'suite'), ('family_room', 'family_room')])),
            ],
            options={
                'verbose_name': 'rewiew',
                'verbose_name_plural': 'rewiews',
                'db_table': 'rewiew',
                'ordering': ['-id'],
            },
        ),
    ]
