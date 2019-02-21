# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_remove_goodssku_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsspu',
            name='image',
            field=models.ImageField(verbose_name='商品图片', upload_to='goods_spu'),
        ),
    ]
