# Generated by Django 5.0.1 on 2024-02-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_issue', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('genre', models.ManyToManyField(to='game_collection.genre')),
            ],
        ),
    ]