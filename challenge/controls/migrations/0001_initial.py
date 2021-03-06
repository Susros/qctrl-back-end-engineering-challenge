# Generated by Django 3.0.2 on 2020-01-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('control_type', models.CharField(choices=[('Primitive', 'Primitive'), ('CORPSE', 'CORPSE'), ('Gaussian', 'Gaussian'), ('CinBB', 'CinBB'), ('CinSK', 'CinSK')], max_length=10)),
                ('maximum_rabi_rate', models.DecimalField(decimal_places=5, max_digits=8)),
                ('polar_angle', models.DecimalField(decimal_places=5, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
