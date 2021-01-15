# Generated by Django 3.1.5 on 2021-01-14 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_practicioner',
        ),
        migrations.CreateModel(
            name='PracticionerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profiles/avatar.png', upload_to='practiconiers')),
                ('field', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pracprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
