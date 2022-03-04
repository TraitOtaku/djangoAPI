# Generated by Django 3.2.9 on 2022-03-04 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Lost', 'Lost')], default='Active', max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '店舗名',
            },
        ),
    ]
