# Generated by Django 4.2.4 on 2023-10-12 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitud', '0001_initial'),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('stock_producto', models.PositiveIntegerField()),
                ('nombre_producto', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='categoria.categoria')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='solicitud.solicitud')),
            ],
            options={
                'db_table': 'producto',
            },
        ),
    ]
