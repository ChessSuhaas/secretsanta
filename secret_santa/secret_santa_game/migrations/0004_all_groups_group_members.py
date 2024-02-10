# Generated by Django 5.0.1 on 2024-01-23 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret_santa_game', '0003_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('min_price', models.IntegerField()),
                ('dead_line', models.DateField()),
                ('create_date', models.DateField()),
                ('special_key', models.CharField(verbose_name=20)),
                ('password', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secret_santa_game.users')),
            ],
        ),
        migrations.CreateModel(
            name='Group_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secret_santa_game.all_groups')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secret_santa_game.users')),
            ],
        ),
    ]