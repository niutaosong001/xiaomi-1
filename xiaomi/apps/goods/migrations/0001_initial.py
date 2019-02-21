# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='商品具体名称', max_length=20)),
                ('price', models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2)),
                ('stock', models.IntegerField(verbose_name='商品库存', default=1)),
                ('sales', models.IntegerField(verbose_name='商品销量', default=0)),
                ('status', models.SmallIntegerField(verbose_name='商品状态', default=1, choices=[(0, '已售罄'), (1, '热卖中')])),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
                'db_table': 'df_goods_sku',
            },
        ),
        migrations.CreateModel(
            name='GoodsSPU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='商品SPU名称', max_length=20)),
                ('detail', tinymce.models.HTMLField(verbose_name='商品详情', blank=True)),
                ('image', models.ImageField(verbose_name='商品图片', upload_to='media')),
            ],
            options={
                'verbose_name': '商品SPU',
                'verbose_name_plural': '商品SPU',
                'db_table': 'df_goods_spu',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='种类名称', max_length=20)),
                ('logo', models.CharField(verbose_name='英文标识', max_length=20)),
            ],
            options={
                'verbose_name': '商品种类',
                'verbose_name_plural': '商品种类',
                'db_table': 'df_goods_type',
            },
        ),
        migrations.CreateModel(
            name='IndexGoodsBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('image', models.ImageField(verbose_name='图片', upload_to='banner')),
                ('index', models.SmallIntegerField(verbose_name='展示顺序', default=0)),
                ('spu', models.ForeignKey(verbose_name='商品SPU', to='goods.GoodsSPU')),
            ],
            options={
                'verbose_name': '首页轮播图商品',
                'verbose_name_plural': '首页轮播图商品',
                'db_table': 'df_index_banner',
            },
        ),
        migrations.AddField(
            model_name='goodsspu',
            name='type',
            field=models.ForeignKey(verbose_name='商品种类', to='goods.GoodsType'),
        ),
        migrations.AddField(
            model_name='goodssku',
            name='spu',
            field=models.ForeignKey(verbose_name='商品SPU', to='goods.GoodsSPU'),
        ),
        migrations.AddField(
            model_name='goodssku',
            name='type',
            field=models.ForeignKey(verbose_name='商品种类', to='goods.GoodsType'),
        ),
    ]
