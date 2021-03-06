# Generated by Django 3.1 on 2020-09-09 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200909_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.author')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.post'),
        ),
    ]
