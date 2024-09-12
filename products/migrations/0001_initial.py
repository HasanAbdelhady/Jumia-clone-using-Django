# Generated by Django 5.1 on 2024-09-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('in_stock', models.BooleanField()),
            ],
        ),
    ]