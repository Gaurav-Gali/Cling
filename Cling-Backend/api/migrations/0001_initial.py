# Generated by Django 4.1.5 on 2023-01-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=10000)),
                ('avatarUrl', models.URLField(max_length=10000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
