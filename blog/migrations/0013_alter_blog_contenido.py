# Generated by Django 4.2.11 on 2024-05-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_contenido_alter_blog_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=models.TextField(blank=True, default=''),
        ),
    ]
