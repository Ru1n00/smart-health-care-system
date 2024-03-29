# Generated by Django 4.2.4 on 2024-02-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_health_care_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ambulance',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='blooddonor',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='blooddonor',
            name='last_donation_date',
            field=models.DateField(blank=True, help_text="Enter donor's last donation date -> 2020-12-31", null=True),
        ),
    ]
