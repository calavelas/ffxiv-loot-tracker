# Generated by Django 3.2.5 on 2021-08-09 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lodestoneId', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('Head', 'Head'), ('Body', 'Body'), ('Hand', 'Hand'), ('Leg', 'Leg'), ('Boot', 'Boot')], max_length=5)),
                ('iLevel', models.CharField(max_length=3)),
                ('isRaid', models.BooleanField(default=True)),
                ('xivApiId', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('DOW', 'Disciple of War'), ('DOM', 'Disciple of Magic')], max_length=3)),
                ('role', models.CharField(choices=[('TANK', 'Tank'), ('HEAL', 'Healer'), ('MELEE', 'Melee DPS'), ('RANGE', 'Range DPS'), ('MAGE', 'Magic DPS')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Patch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.character')),
            ],
        ),
        migrations.CreateModel(
            name='StaticMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.job')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.character')),
                ('static', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.static')),
            ],
        ),
        migrations.CreateModel(
            name='StaticBIS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.staticmember')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.item')),
                ('patch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.patch')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='patch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot_tracker.patch'),
        ),
    ]
