# Generated by Django 4.2 on 2023-04-16 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=128, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, null=True, verbose_name='Last Name')),
                ('contact_number', models.BigIntegerField(null=True, verbose_name='Contact Number')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Time of Commute')),
                ('start_latitude', models.FloatField(blank=True, verbose_name='Starting Place Latitude')),
                ('start_longitude', models.FloatField(blank=True, verbose_name='Starting Place Longitude')),
                ('start_name', models.TextField(blank=True, verbose_name='Starting Place')),
                ('end_latitude', models.FloatField(blank=True, verbose_name='Ending Place Latitude')),
                ('end_longitude', models.FloatField(blank=True, verbose_name='Ending Place Longitude')),
                ('end_name', models.TextField(blank=True, verbose_name='Ending Place Name')),
                ('seats', models.IntegerField()),
                ('participants', models.ManyToManyField(blank=True, related_name='trips', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts_trip', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
