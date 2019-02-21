from django.db import models
from db.base_model import base_model as BaseModel
from tinymce.models import HTMLField

#商品种类
class GoodsType(BaseModel):
    name=models.CharField(max_length=20,verbose_name="种类名称")
    logo=models.CharField(max_length=20,verbose_name="英文标识")
    class Meta:
        db_table ="df_goods_type"
        verbose_name="商品种类"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

#商品spu
class GoodsSPU(BaseModel):
    name=models.CharField(max_length=20,verbose_name="商品SPU名称")
    type=models.ForeignKey(GoodsType,verbose_name="商品种类")
    detail = HTMLField(blank=True,verbose_name="商品详情")
    image=models.ImageField(upload_to="goods_spu",verbose_name="商品图片")
    def __str__(self):
        return self.name

    class Meta:
        db_table="df_goods_spu"
        verbose_name="商品SPU"
        verbose_name_plural=verbose_name

#商品sku
class GoodsSKU(BaseModel):
    status_choices=(
        (0,"已售罄"),
        (1,"热卖中")
    )
    spu =models.ForeignKey(GoodsSPU,verbose_name="商品SPU")
    name=models.CharField(max_length=20,verbose_name="商品具体名称")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="商品价格")
    stock=models.IntegerField(default=1,verbose_name="商品库存")
    sales=models.IntegerField(default=0,verbose_name="商品销量")
    status=models.SmallIntegerField(default=1,choices=status_choices,verbose_name="商品状态")
    def __str__(self):
        return self.name
    class Meta:
        db_table="df_goods_sku"
        verbose_name="商品SKU"
        verbose_name_plural=verbose_name

#首页商品轮播图
class IndexGoodsBanner(BaseModel):
    spu=models.ForeignKey("GoodsSPU",verbose_name="商品SPU")
    image= models.ImageField(upload_to="banner",verbose_name="图片")
    index =models.SmallIntegerField(default=0,verbose_name="展示顺序")
    def __str__(self):
        return self.spu.name
    class Meta:
        db_table="df_index_banner"
        verbose_name="首页轮播图商品"
        verbose_name_plural=verbose_name


