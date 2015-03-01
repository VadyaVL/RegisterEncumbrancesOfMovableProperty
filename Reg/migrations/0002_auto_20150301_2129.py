# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encumbrance',
            name='SPerson',
            field=models.ManyToManyField(related_name='S', to='Reg.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encumbrance',
            name='WPerson',
            field=models.ManyToManyField(related_name='W', to='Reg.Person'),
            preserve_default=True,
        ),
    ]
