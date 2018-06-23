# Generated by Django 2.0.6 on 2018-06-12 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nusid', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=30, unique=True)),
                ('tutorialgroup', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='student_of',
            field=models.ManyToManyField(to='attendance.Tutorial'),
        ),
        migrations.AddField(
            model_name='session',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutorials', to='attendance.Tutorial'),
        ),
    ]
