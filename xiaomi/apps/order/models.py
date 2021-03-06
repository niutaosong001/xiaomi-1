from django.db import models
# Create your models here.
from db.base_model import base_model as BaseModel


#订单信息
class OrderInfo(BaseModel):
    PAY_METHOD_CHOICES=(
        (1,"货到付款"),
        (2,"微信支付"),
        (3,"支付宝"),
        (4,"银联支付")
    )
    ORDER_STATUS_CHOICES=(
        (1,"待支付"),
        (2,"待发货"),
        (3,"待收货"),
        (4,"待评价"),
        (5,"已完成")
    )

    # PAY_METHODS = {
    #     '1': "货到付款",
    #     '2': "微信支付",
    #     '3': "支付宝",
    #     '4': "银联支付"
    # }
    # PAY_METHODS_ENUM = {
    #     "CASH": 1,
    #     "ALIPAY": 2
    # }
    # ORDER_STATUS_ENUM = {
    #     "UNPAID": 1,
    #     "UNSEND": 2,
    #     "UNRECEIVED": 3,
    #     "UNCOMMENT": 4,
    #     "FINISHED": 5
    # }
    # ORDER_STATUS = {
    #     1: "待支付",
    #     2: "待发货",
    #     3: "待收货",
    #     4: "待评价",
    #     5: "已完成"
    # }

    order_num=models.CharField(max_length=128,primary_key=True,verbose_name="订单号")
    user=models.ForeignKey("user.User",verbose_name="所属用户")
    addr=models.ForeignKey("user.Address",verbose_name="收货地址")
    pay_method=models.SmallIntegerField(choices=PAY_METHOD_CHOICES,default=3,verbose_name="支付方式")
    total_count=models.IntegerField(default=1,verbose_name="商品数量")
    total_price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="商品总价")
    transit_price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="订单运费")
    order_status=models.SmallIntegerField(choices=ORDER_STATUS_CHOICES,default=1,verbose_name="订单状态")
    trade_no = models.CharField(max_length=128,default="",verbose_name="支付编号")
    comment=models.CharField(max_length=256,verbose_name="订单评论",default="")
    class Meta:
        db_table="df_order_info"
        verbose_name="订单信息"
        verbose_name_plural=verbose_name


#订单商品
class OrderGoods(BaseModel):
    order=models.ForeignKey("OrderInfo",verbose_name="订单")
    sku=models.ForeignKey("goods.GoodsSKU",verbose_name="商品SKU")
    count=models.IntegerField(default=1,verbose_name="商品数目")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="商品价格")
    class Meta:
        db_table="df_order_goods"
        verbose_name="订单商品"
        verbose_name_plural=verbose_name
