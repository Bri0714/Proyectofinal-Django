# Generated by Django 4.1.3 on 2022-12-10 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0006_remove_empresa_nombre_empresa_empresa_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='nombre',
            new_name='nombre_empresa',
        ),
    ]