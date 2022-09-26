from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name='Категория',max_length=100, null=False, blank=False, default="No category")
    description = models.TextField(verbose_name='Описание',max_length=500, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} - {self.description}"

class Good(models.Model):
    title = models.CharField(verbose_name='Наименование',max_length=100, null=False, blank=False, default="No title")
    description = models.TextField(verbose_name='Описание',max_length=500, null=True, default="No description")
    category = models.ForeignKey(verbose_name="Категория", to='shop_app.Category', null=False, blank=False, related_name='goods', on_delete=models.CASCADE, )
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2, null=False)
    photo = models.ImageField(verbose_name="Изображение", )
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.price}"