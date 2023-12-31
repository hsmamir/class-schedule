# Generated by Django 3.2.2 on 2023-07-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('theory_course', models.IntegerField()),
                ('practical_course', models.IntegerField()),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projection.field')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date_of_week', models.PositiveSmallIntegerField(choices=[(0, 'sat'), (1, 'sun'), (2, 'mon'), (3, 'tue'), (4, 'wed'), (5, 'thu'), (6, 'fri')])),
                ('capacity', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projection.exam')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projection.lesson')),
                ('plato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projection.plato')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.profile')),
            ],
        ),
    ]
