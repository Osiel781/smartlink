# Generated by Django 2.1.7 on 2019-06-26 05:44

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0040_auto_20190626_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='relacion_tec',
            field=models.CharField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('Empleado Tec', 'Empleado Tec'), ('Padre/Madre Tec', 'Padre/Madre Tec'), ('Ninguna', 'Ninguna')], default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='tipo_invitacion',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('Empleado Tec', 'Empleado Tec'), ('Padre/Madre Tec', 'Padre/Madre Tec'), ('General', 'General')], default=None, max_length=122),
        ),
    ]
