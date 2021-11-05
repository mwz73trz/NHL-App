# Generated by Django 3.2.9 on 2021-11-05 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='nhl_app.conference')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gp', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('ot', models.IntegerField(default=0)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='nhl_app.conference')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='nhl_app.division')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='nhl_app.league')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gp', models.IntegerField(default=0)),
                ('goals', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='nhl_app.conference')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='nhl_app.division')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='nhl_app.league')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='nhl_app.team')),
            ],
        ),
        migrations.AddField(
            model_name='division',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='nhl_app.league'),
        ),
        migrations.AddField(
            model_name='conference',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conferences', to='nhl_app.league'),
        ),
    ]
