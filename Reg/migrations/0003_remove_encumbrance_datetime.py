# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reg', '0002_auto_20150301_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encumbrance',
            name='DateTime',
        ),
    ]
