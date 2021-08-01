# Generated by Django 3.0 on 2021-08-01 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=100)),
                ('Company_address', models.TextField()),
                ('person_name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('date_time', models.TextField()),
                ('Comment_remark', models.TextField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Employee')),
            ],
        ),
    ]
