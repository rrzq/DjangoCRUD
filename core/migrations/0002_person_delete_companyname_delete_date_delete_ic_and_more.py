# Generated by Django 4.1.5 on 2023-04-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('companyname', models.CharField(max_length=100)),
                ('ic', models.CharField(max_length=15)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Companyname',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='IC',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]