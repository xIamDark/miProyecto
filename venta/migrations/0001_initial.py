# Generated by Django 4.1.2 on 2023-06-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_producto', models.AutoField(db_column='tipoProducto', primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_llegada', models.DateField()),
                ('activo', models.IntegerField()),
                ('tipo_producto', models.ForeignKey(db_column='tipoProducto', on_delete=django.db.models.deletion.CASCADE, to='venta.producto')),
            ],
        ),
    ]
