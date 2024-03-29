# Generated by Django 2.2.2 on 2019-06-23 03:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20190623_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Action ', 'Action'), ('Adventure ', 'Adventure'), ('Anime ', 'Anime'), ('Racing ', 'Racing'), ('RPG ', 'RPG'), ('Simulation ', 'Simulation'), ('Sport ', 'Sport'), ('Strategy ', 'Strategy'), ('Survival ', 'Survival'), ('VR ', 'VR'), ('Horror ', 'Horror'), ('Shooter ', 'Shooter'), ('Puzzle ', 'Puzzle'), ('OpenWorld ', 'OpenWorld'), ('VisualNovel ', 'VisualNovel')], max_length=130),
        ),
    ]
