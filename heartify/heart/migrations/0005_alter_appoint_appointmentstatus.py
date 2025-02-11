# Generated by Django 4.1.1 on 2024-04-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0004_doctorsugg_designation_doctorsugg_state_appoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointmentstatus',
            field=models.CharField(choices=[('Rej', 'Rejected'), ('Pen', 'Pending'), ('Conf', 'Confirmed'), ('Prog', 'In Progress'), ('Comp', 'Completed')], default='Pen', max_length=50),
        ),
    ]
