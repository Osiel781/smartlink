# Generated by Django 2.1.7 on 2019-06-25 04:46

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0036_auto_20190620_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='tipo_invitacion',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('2', 'Empleado Tec'), ('3', 'Papa/Mama Tec'), ('General', 'General')], default=None, max_length=97),
        ),
    ]
