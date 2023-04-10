# Generated by Django 3.2.18 on 2023-04-10 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(blank='True', max_length=250)),
                ('pwd', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('lungs', 'lungs'), ('Brain', 'Brain'), ('Bone', 'Bone'), ('heart', 'heart')], max_length=250)),
                ('exp', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(blank=True, max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('apoinment', models.TimeField(max_length=40)),
                ('date', models.DateField(max_length=50)),
                ('issue', models.CharField(max_length=250)),
                ('Doctor', models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='activity',
            fields=[
                ('Patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.patient')),
                ('confirm', models.BooleanField(default=False, max_length=20)),
                ('date_time', models.DateTimeField()),
                ('data', models.FileField(blank=True, upload_to='files')),
            ],
        ),
    ]