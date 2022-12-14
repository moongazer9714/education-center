# Generated by Django 4.1.4 on 2022-12-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('image', models.ImageField(upload_to='teacher/')),
                ('role', models.CharField(max_length=221)),
                ('bio', models.TextField()),
                ('social_telegram', models.CharField(blank=True, max_length=200, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('social_facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('social_instagram', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
