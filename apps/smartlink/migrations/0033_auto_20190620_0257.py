# Generated by Django 2.1.7 on 2019-06-20 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0032_eventos_prioridad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='relacion_tec',
            field=models.CharField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('Empleado Tec', 'Empleado Tec'), ('Papa/Mama Tec', 'Papá/Mamá Tec'), ('Ninguna', 'Ninguna')], default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='user',
            field=models.OneToOneField(blank=True, error_messages={'unique': 'This email has already been registered.'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='prioridad',
            field=models.CharField(choices=[('alta', 'alta'), ('normal', 'normal'), ('ninguna', 'ninguna')], default=None, max_length=200),
        ),
    ]