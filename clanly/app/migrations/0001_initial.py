<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-11-15 05:07
=======
# Generated by Django 4.1.1 on 2022-11-15 05:56
>>>>>>> 3192d6d43fc02890b0256b477a2016380cc69ad7

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
            name='Community',
            fields=[
<<<<<<< HEAD
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_community', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('communityimg', models.ImageField(default='blank-profile-picture.png', upload_to='community_images/')),
                ('background', models.ImageField(default='blank-profile-picture.png', upload_to='community_images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('private', models.BooleanField(default=False)),
                ('admins', models.ManyToManyField(blank=True, related_name='admins', to=settings.AUTH_USER_MODEL)),
                ('banned', models.ManyToManyField(blank=True, related_name='banned', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
=======
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                (
                    "communityimg",
                    models.ImageField(
                        default="blank-profile-picture.png",
                        upload_to="community_images/",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("private", models.BooleanField(default=False)),
                (
                    "admins",
                    models.ManyToManyField(
                        blank=True, related_name="admins", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "banned",
                    models.ManyToManyField(
                        blank=True, related_name="banned", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        blank=True, related_name="members", to=settings.AUTH_USER_MODEL
                    ),
                ),
>>>>>>> 3192d6d43fc02890b0256b477a2016380cc69ad7
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
<<<<<<< HEAD
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('fname', models.CharField(max_length=30)),
                ('profile_img', models.ImageField(blank=True, default='blank-profile-picture.png', upload_to='profile_images/')),
                ('cover_img', models.ImageField(blank=True, default='blank-cover-picture.png', upload_to='cover_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_user", models.IntegerField()),
                ("bio", models.TextField(blank=True, null=True)),
                ("fname", models.CharField(max_length=30)),
                (
                    "profile_img",
                    models.ImageField(
                        blank=True,
                        default="blank-profile-picture.png",
                        upload_to="profile_images/",
                    ),
                ),
                (
                    "cover_img",
                    models.ImageField(
                        blank=True,
                        default="blank-cover-picture.png",
                        upload_to="cover_images/",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
>>>>>>> 3192d6d43fc02890b0256b477a2016380cc69ad7
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
<<<<<<< HEAD
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('id_post', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('postimg', models.ImageField(default='blank-profile-picture.png', upload_to='post_images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.community')),
=======
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                (
                    "postimg",
                    models.ImageField(
                        default="blank-profile-picture.png", upload_to="post_images/"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "community",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.community"
                    ),
                ),
>>>>>>> 3192d6d43fc02890b0256b477a2016380cc69ad7
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_comment', models.IntegerField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
