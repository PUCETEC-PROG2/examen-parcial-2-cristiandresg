from django.db import migrations, models

class Migration(migrations.Migration):
    
    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_genre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_movie',
            field=models.CharField(max_length=30),
        ),
    ]
