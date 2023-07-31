# Generated by Django 4.2.3 on 2023-07-31 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_plant_country_of_origin_growthcondition_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='growthcondition',
            name='description',
        ),
        migrations.RemoveField(
            model_name='growthcondition',
            name='name',
        ),
        migrations.RemoveField(
            model_name='growthcondition',
            name='plants',
        ),
        migrations.AddField(
            model_name='growthcondition',
            name='category',
            field=models.CharField(choices=[('light', 'Light'), ('water', 'Water'), ('air', 'Air'), ('nutrients', 'Nutrients'), ('temperature', 'Temperature')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='growthcondition',
            name='descriptor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='growth_conditions',
            field=models.ManyToManyField(to='main_app.growthcondition'),
        ),
    ]
