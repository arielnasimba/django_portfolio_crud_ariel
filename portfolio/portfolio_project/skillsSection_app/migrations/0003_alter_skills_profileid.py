# Generated by Django 4.2.11 on 2024-05-03 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0001_initial'),
        ('skillsSection_app', '0002_skills_profileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='profileID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='about_app.profile'),
        ),
    ]
