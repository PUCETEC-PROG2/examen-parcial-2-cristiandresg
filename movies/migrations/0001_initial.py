from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title_movie', models.CharField(max_length=50)),
                ('movie_genre', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('release_year', models.DateField()),
                ('sinopsis', models.TextField()),
            ],
        ),
    ]
    