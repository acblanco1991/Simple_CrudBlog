# Generated by Django 4.2.11 on 2024-05-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_blog_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
