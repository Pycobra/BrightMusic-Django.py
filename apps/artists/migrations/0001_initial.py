# Generated by Django 3.2.8 on 2022-10-03 08:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('release_year', models.DateField()),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('format', models.CharField(max_length=50, verbose_name='Format')),
                ('minutes', models.CharField(max_length=50, verbose_name='Minutes')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_songs', to='artists.artist', verbose_name='Artist')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.CreateModel(
            name='ArtistImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='images/others/igor-lypnytskyi-PobecUzsK4c-unsplash.png', help_text='Upload a artist image', upload_to='images/uploads/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_images', to='artists.artist', verbose_name='Artist')),
            ],
            options={
                'verbose_name': 'Artist Image',
                'verbose_name_plural': 'Artist Images',
            },
        ),
    ]
