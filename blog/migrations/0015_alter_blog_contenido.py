# Generated by Django 4.2.11 on 2024-05-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_blog_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
    ]
