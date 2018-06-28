# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0007_auto_20171031_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='website',
            field=models.URLField(help_text='URL-\u0430\u0434\u0440\u0435\u0441 \u0432\u0435\u0431-\u0441\u0430\u0439\u0442\u0430, \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0441 \u044d\u0442\u0438\u043c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c API.'),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='website',
            field=models.URLField(help_text='URL-\u0430\u0434\u0440\u0435\u0441 \u0432\u0435\u0431-\u0441\u0430\u0439\u0442\u0430, \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0441 \u044d\u0442\u0438\u043c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c API.'),
        ),
    ]
