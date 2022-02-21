# Generated by Django 3.2.9 on 2022-02-21 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=100)),
                ('suite', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Lost', 'Lost')], default='Active', max_length=30)),
                ('contact', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '企業名',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=100)),
                ('suite', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Lost', 'Lost')], default='Active', max_length=30)),
                ('contact', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.company')),
            ],
            options={
                'verbose_name_plural': '店舗名',
            },
        ),
    ]