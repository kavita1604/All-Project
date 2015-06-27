# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('answer_text', models.CharField(max_length=150)),
                ('no_of_votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='src.Question')),
            ],
        ),
    ]
