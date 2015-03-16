# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Address',
            field=models.ForeignKey(to='Reg.Address', null=True),
            preserve_default=True,
        ),
    ]
