from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_director_alter_movie_movie_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_genre',
            field=models.CharField(choices=[('A', 'Accion'), ('B', 'Biografia'), ('C', 'COmedia'), ('T', 'Terror')], max_length=30),
        ),
    ]
    