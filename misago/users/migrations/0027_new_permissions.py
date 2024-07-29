# Generated by Django 4.2.7 on 2023-12-21 21:10

import django.contrib.postgres.fields
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("misago_users", "0026_plugin_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("slug", models.CharField(max_length=150, unique=True)),
                ("user_title", models.CharField(blank=True, max_length=150, null=True)),
                ("color", models.CharField(blank=True, max_length=7, null=True)),
                ("icon", models.CharField(blank=True, max_length=50, null=True)),
                ("css_suffix", models.CharField(blank=True, max_length=50, null=True)),
                ("is_page", models.BooleanField(default=False)),
                ("is_hidden", models.BooleanField(default=False)),
                ("is_default", models.BooleanField(default=False)),
                ("ordering", models.PositiveIntegerField(default=0)),
                ("can_use_private_threads", models.BooleanField(default=False)),
                ("can_change_username", models.BooleanField(default=False)),
                ("username_changes_limit", models.PositiveIntegerField(default=0)),
                ("username_changes_expire", models.PositiveIntegerField(default=0)),
                ("username_changes_span", models.PositiveIntegerField(default=0)),
                ("can_see_user_profiles", models.BooleanField(default=False)),
                ("plugin_data", models.JSONField(default=dict)),
            ],
            options={"ordering": ["ordering"]},
        ),
        migrations.AddIndex(
            model_name="group",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["plugin_data"], name="misago_user_plugin__e41d7b_gin"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups_ids",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveIntegerField(), default=list, size=None
            ),
        ),
        migrations.AddIndex(
            model_name="user",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["groups_ids"], name="misago_user_groups_ids"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="misago_users.group",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="permissions_id",
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_misago_root",
            field=models.BooleanField(default=False),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(
                condition=models.Q(("is_misago_root", True)),
                fields=["is_misago_root"],
                name="misago_user_is_misago_root",
            ),
        ),
        migrations.CreateModel(
            name="GroupDescription",
            fields=[
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        primary_key=True,
                        related_name="description",
                        serialize=False,
                        to="misago_users.group",
                    ),
                ),
                ("markdown", models.TextField(blank=True, null=True)),
                ("html", models.TextField(blank=True, null=True)),
                ("meta", models.TextField(blank=True, null=True)),
                ("plugin_data", models.JSONField(default=dict)),
            ],
            options={
                "abstract": False,
                "indexes": [
                    django.contrib.postgres.indexes.GinIndex(
                        fields=["plugin_data"], name="misago_user_plugin__065d95_gin"
                    )
                ],
            },
        ),
    ]