# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reg', '0003_remove_encumbrance_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='MoreInformation',
            field=models.CharField(max_length=500, null=True, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4. \xd1\x96\xd0\xbd\xd1\x84.', db_column=b'MoreInformation'),
            preserve_default=True,
        ),
    ]
