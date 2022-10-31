# Generated by Django 4.1.2 on 2022-10-30 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='Project_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.client'),
        ),
    ]
