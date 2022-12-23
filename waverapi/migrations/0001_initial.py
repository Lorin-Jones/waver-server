# Generated by Django 4.1.3 on 2022-12-23 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='GearType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserGear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_gear', to='waverapi.gear')),
            ],
        ),
        migrations.CreateModel(
            name='WaverUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('gear', models.ManyToManyField(through='waverapi.UserGear', to='waverapi.gear')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usergear',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gear_user', to='waverapi.waveruser'),
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.IntegerField()),
                ('number_of_keys', models.CharField(blank=True, max_length=50, null=True)),
                ('voices', models.CharField(blank=True, max_length=50, null=True)),
                ('arpeggiator', models.BooleanField(blank=True, default=None, null=True)),
                ('sequencer', models.BooleanField(blank=True, default=None, null=True)),
                ('velocity', models.BooleanField(blank=True, default=None, null=True)),
                ('aftertouch', models.BooleanField(blank=True, default=None, null=True)),
                ('gear_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverapi.geartype')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverapi.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('created_on', models.DateField()),
                ('waver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverapi.waveruser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='waverapi.waveruser')),
            ],
        ),
        migrations.CreateModel(
            name='GearReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverapi.gear')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverapi.review')),
            ],
        ),
        migrations.AddField(
            model_name='gear',
            name='reviews',
            field=models.ManyToManyField(related_name='gear_reviews', through='waverapi.GearReview', to='waverapi.review'),
        ),
        migrations.AddField(
            model_name='gear',
            name='specifications',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverapi.specification'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='waverapi.waveruser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='waverapi.post')),
            ],
        ),
    ]
