# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reg', '0002_auto_20150316_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofencumbrance',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, db_column=b'id'),
            preserve_default=True,
        ),
    ]
