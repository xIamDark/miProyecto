# Generated by Django 4.1.2 on 2023-06-05 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_rename_activo_producto_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoproducto',
            old_name='producto',
            new_name='tipo',
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='venta.tipoproducto'),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='id_producto',
            field=models.AutoField(db_column='id_producto', primary_key=True, serialize=False),
        ),
    ]
