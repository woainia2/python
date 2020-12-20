from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """图书信息"""
    title = models.CharField(max_length=20, verbose_name='标题')
    pub_date = models.DateField(verbose_name='发布日期')
    image = models.ImageField(upload_to='avatar',verbose_name='图书封面')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="价格")
    read = models.IntegerField(verbose_name='阅读量')
    comment = models.IntegerField(verbose_name='评论量')
    class Meta:
        # db_table = "表名"
        db_table = "tb_book_info"
        verbose_name = "图书"
        verbose_name_plural = verbose_name


    @property
    def text(self):
        return 100