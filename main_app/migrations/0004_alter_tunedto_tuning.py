# Generated by Django 4.0.6 on 2022-07-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_tunedto_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tunedto',
            name='tuning',
            field=models.CharField(choices=[('EADGBE', 'Standard'), ('DADGBE', 'Drop D'), ('EbAbDbGbBbEb', 'Half Step Down'), ('DADGAD', 'Dad Gad')], default='EADGBE', max_length=24),
        ),
    ]
