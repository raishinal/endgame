# Generated by Django 2.2.2 on 2019-06-21 12:35

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'verbose_name_plural': 'games'},
        ),
        migrations.AlterField(
            model_name='games',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Anime', 'Anime'), ('Racing', 'Racing'), ('RPG', 'RPG'), ('Simulation', 'Simulation'), ('Sport', 'Sport'), ('Strategy', 'Strategy'), ('Survival', 'Survival'), ('VR', 'VR'), ('Horror', 'Horror'), ('Shooter', 'Shooter'), ('Puzzle', 'Puzzle'), ('OpenWorld', 'OpenWorld'), ('VisualNovel', 'VisualNovel')], max_length=115),
        ),
        migrations.AlterField(
            model_name='games',
            name='platform',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('PC', 'PC'), ('PS4', 'PS4'), ('Xbox', 'Xbox')], max_length=11),
        ),
    ]
