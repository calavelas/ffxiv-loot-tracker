# Generated by Django 3.2.5 on 2021-08-09 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loot_tracker', '0002_staticloothistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticbis',
            old_name='character',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='staticloothistory',
            old_name='character',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='staticmember',
            old_name='member',
            new_name='character',
        ),
    ]
