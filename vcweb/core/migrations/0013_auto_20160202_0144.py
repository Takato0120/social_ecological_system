# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-02 01:44


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_null_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='status',
            field=models.CharField(choices=[(b'INACTIVE', 'Not active'), (b'ACTIVE', 'Active, no round in progress'), (b'ROUND_IN_PROGRESS', 'Round in progress'), (b'COMPLETED', 'Completed'), (b'PUBLISHED', 'Published')], default=b'INACTIVE', max_length=32),
        ),
    ]
