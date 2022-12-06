# Generated by Django 4.1.3 on 2022-12-05 08:12

from django.db import migrations, models
import game_check.game_review.validators


class Migration(migrations.Migration):

    dependencies = [
        ('game_review', '0016_alter_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars', validators=[game_check.game_review.validators.validate_file_less_than_one]),
        ),
    ]