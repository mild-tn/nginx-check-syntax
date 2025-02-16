# Generated by Django 3.0 on 2020-05-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Redirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=250)),
                ('rule', models.CharField(max_length=250)),
                ('redirect_to', models.CharField(max_length=250)),
                ('is_permanent', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_http_to_https', models.BooleanField(default=False)),
            ],
        ),
    ]
