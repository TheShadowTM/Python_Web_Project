# Generated by Django 4.1.3 on 2022-12-01 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import game_check.game_review.validators


class Migration(migrations.Migration):

    dependencies = [
        ('game_review', '0003_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(validators=[game_check.game_review.validators.score_validator])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
