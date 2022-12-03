# Generated by Django 4.1.3 on 2022-12-02 12:43

from django.db import migrations, models
import game_check.game_review.validators


class Migration(migrations.Migration):

    dependencies = [
        ('game_review', '0009_game_game_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='./mediafiles/temp-default.jpg', upload_to='avatars/', validators=[game_check.game_review.validators.validate_file_less_than_one]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='None', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('DoNotShow', 'Do not show')], default='Male', max_length=9),
        ),
    ]
