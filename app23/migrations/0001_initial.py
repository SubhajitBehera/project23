# Generated by Django 3.0.4 on 2020-04-01 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('acno', models.IntegerField(primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=30)),
                ('ifsc', models.CharField(max_length=30)),
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app23.Employee')),
            ],
        ),
    ]