# Generated by Django 4.2.11 on 2030-11-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_nombre_blog_categorias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='contenido',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
