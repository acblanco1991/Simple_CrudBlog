# Generated by Django 4.2.11 on 2024-05-15 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_categoria_descripcion_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.categoria'),
        ),
    ]
