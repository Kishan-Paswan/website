# Generated by Django 4.2 on 2023-10-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicesmodel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'db_table': 'servicetb',
            },
        ),
    ]
