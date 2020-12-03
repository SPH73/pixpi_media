# Generated by Django 3.1.3 on 2020-12-03 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='private',
            options={'verbose_name_plural': 'Private Albums'},
        ),
        migrations.AlterModelOptions(
            name='public',
            options={'verbose_name_plural': 'Public Albums'},
        ),
        migrations.AlterField(
            model_name='private',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='private_albums', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='public',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_albums', to='profiles.profile'),
        ),
    ]
