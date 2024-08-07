# Generated by Django 4.2.13 on 2024-06-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_director_movieinfo_directed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='acted_by',
            field=models.ManyToManyField(related_name='acted_movies', to='movie_app.actor'),
        ),
    ]
