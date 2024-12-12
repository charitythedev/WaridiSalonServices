# Generated by Django 5.0.7 on 2024-12-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_rename_phonenumber_contactrequest_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]