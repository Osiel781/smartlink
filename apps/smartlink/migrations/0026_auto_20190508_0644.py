# Generated by Django 2.1.7 on 2019-05-08 06:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0025_auto_20190508_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='tipo_invitacion',
        ),
        migrations.AddField(
            model_name='eventos',
            name='tipo_invitacion',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('Empleado Tec', 'Empleado Tec'), ('Papá/Mamá Tec', 'Papá/Mamá Tec'), ('Ninguna', 'Ninguna')], default=None, max_length=120),
        ),
        migrations.DeleteModel(
            name='Tipo_invitacion',
        ),
    ]
