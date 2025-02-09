# Generated by Django 5.1.6 on 2025-02-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('type', models.CharField(choices=[('image', 'image'), ('video', 'video'), ('audio', 'audio'), ('file', 'file')], default='image', max_length=15)),
                ('path', models.CharField(max_length=1000)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
