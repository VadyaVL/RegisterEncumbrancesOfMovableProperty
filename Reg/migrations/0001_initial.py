# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Country', models.CharField(default=b'Ukraine', max_length=45, verbose_name=b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x97\xd0\xbd\xd0\xb0', db_column=b'Country')),
                ('Index', models.CharField(max_length=45, verbose_name=b'\xd0\x86\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xba\xd1\x81', db_column=b'Index')),
                ('Region', models.CharField(max_length=45, verbose_name=b'\xd0\x9e\xd0\xb1\xd0\xbb\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c', db_column=b'Region')),
                ('Area', models.CharField(max_length=45, null=True, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd', db_column=b'Area')),
                ('City', models.CharField(max_length=45, verbose_name=b'\xd0\x9c\xd1\x96\xd1\x81\xd1\x82\xd0\xbe/\xd0\xbd.\xd0\xbf.', db_column=b'City')),
                ('Street', models.CharField(max_length=45, verbose_name=b'\xd0\x92\xd1\x83\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8f', db_column=b'Street')),
                ('Home', models.CharField(max_length=45, verbose_name=b'\xd0\xb4\xd1\x96\xd0\xbc/\xd0\xb1\xd1\x83\xd0\xb4.', db_column=b'Home')),
            ],
            options={
                'db_table': 'Address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=45, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0', db_column=b'Name')),
                ('Number', models.CharField(max_length=45, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80', db_column=b'Number')),
                ('Date', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0', db_column=b'Date')),
                ('PublisherName', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd1\x83\xd0\xb1\xd0\xbb\xd1\x96\xd0\xba\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80', db_column=b'PublisherName')),
            ],
            options={
                'db_table': 'DocumentBase',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Encumbrance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DateTime', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd0\xbd\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', db_column=b'DateTime')),
                ('NStatement', models.IntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xb8', db_column=b'NStatement')),
                ('DateStatement', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xb8', db_column=b'DateStatement')),
                ('Date', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0', db_column=b'Date')),
                ('AddedInfo', models.CharField(max_length=500, null=True, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4. \xd1\x96\xd0\xbd\xd1\x84.', db_column=b'AddedInfo')),
            ],
            options={
                'db_table': 'Encumbrance',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=45, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0', db_column=b'Name')),
                ('SerialNumber', models.CharField(max_length=45, verbose_name=b'\xd0\xa1\xd0\xb5\xd1\x80\xd1\x96\xd0\xb9\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80', db_column=b'SerialNumber')),
                ('RegNumber', models.CharField(max_length=45, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x80\xd0\xb5\xd1\x94\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd1\x96\xd1\x97', db_column=b'RegNumber')),
                ('AddedInfoForUNMovable', models.CharField(max_length=500, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4. \xd1\x96\xd0\xbd\xd1\x84.(\xd0\xbd\xd0\xb5\xd1\x80\xd1\x83\xd1\x85\xd0\xbe\xd0\xbc\xd0\xb5)', db_column=b'AddedInfoForUNMovable')),
                ('Encumbrance', models.OneToOneField(to='Reg.Encumbrance')),
            ],
            options={
                'db_table': 'Object',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Identification', models.CharField(max_length=10, verbose_name=b'\xd0\x86\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x84\xd1\x96\xd0\xba\xd0\xb0\xd1\x86\xd1\x96\xd0\xb9\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80', db_column=b'Identification')),
                ('NonResidentForeigner', models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb7\xd0\xb8\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82', db_column=b'NonResidentForeigner')),
                ('Name', models.CharField(max_length=100, verbose_name=b'\xd0\xa4.\xd0\x86.\xd0\x9e.', db_column=b'Name')),
                ('MoreInformation', models.CharField(max_length=500, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4. \xd1\x96\xd0\xbd\xd1\x84.', db_column=b'MoreInformation')),
                ('Address', models.ForeignKey(to='Reg.Address')),
            ],
            options={
                'db_table': 'Person',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SizeObligations', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb7\xd0\xbc\xd1\x96\xd1\x80 \xd0\xbe\xd0\xb1\xd0\xbb\xd1\x96\xd0\xb3\xd0\xb0\xd1\x86\xd1\x96\xd1\x97', db_column=b'SizeObligations')),
                ('LimitDate', models.DateField(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xbe\xd0\xba', db_column=b'LimitDate')),
                ('AddedInfo', models.CharField(max_length=500, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4. \xd1\x96\xd0\xbd\xd1\x84.', db_column=b'AddedInfo')),
                ('Encumbrance', models.OneToOneField(to='Reg.Encumbrance')),
            ],
            options={
                'db_table': 'Terms',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeOfCurrency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=45, verbose_name=b'\xd0\x92\xd0\xb0\xd0\xbb\xd1\x8e\xd1\x82\xd0\xb0', db_column=b'Name')),
            ],
            options={
                'db_table': 'TypeOfCurrency',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeOfEncumbrance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=45, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', db_column=b'Name')),
            ],
            options={
                'db_table': 'TypeOfEncumbrance',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeReg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=45, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd1\x80\xd0\xb5\xd1\x94\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd1\x96\xd1\x97', db_column=b'Name')),
            ],
            options={
                'db_table': 'TypeReg',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ViewEncumbrance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=45, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4', db_column=b'Name')),
            ],
            options={
                'db_table': 'ViewEncumbrance',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='terms',
            name='TypeOfCurrency',
            field=models.ForeignKey(to='Reg.TypeOfCurrency'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encumbrance',
            name='TypeOfEncumbrance',
            field=models.ForeignKey(to='Reg.TypeOfEncumbrance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encumbrance',
            name='TypeReg',
            field=models.ForeignKey(to='Reg.TypeReg'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encumbrance',
            name='ViewEncumbrance',
            field=models.ForeignKey(to='Reg.ViewEncumbrance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentbase',
            name='Encumbrance',
            field=models.OneToOneField(to='Reg.Encumbrance'),
            preserve_default=True,
        ),
    ]
