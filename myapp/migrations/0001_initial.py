# Generated by Django 3.0 on 2021-08-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('status', models.CharField(default='inactive', max_length=100)),
                ('usertype', models.CharField(default='user', max_length=100)),
            ],
        ),
    ]