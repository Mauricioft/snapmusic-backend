# Generated by Django 2.1.1 on 2018-11-23 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='catalogs.Artist'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='gender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='catalogs.Gender'),
        ),
        migrations.AddField(
            model_name='user_artist',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_artist', to='catalogs.Artist'),
        ),
        migrations.AddField(
            model_name='user_artist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_artist', to=settings.AUTH_USER_MODEL),
        ),
    ]
