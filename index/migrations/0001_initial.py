# Generated by Django 3.0.5 on 2020-04-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(default='', max_length=20)),
                ('faces', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
