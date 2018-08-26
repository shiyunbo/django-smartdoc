from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os
import uuid


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "picture"
    if ext.lower() in ["pdf", "docx", "txt"]:
        sub_folder = "document"
    return os.path.join(str(instance.author.id), sub_folder, filename)


class AbstractModel(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Product(AbstractModel):
    """产品"""
    name = models.TextField(max_length=30, verbose_name='Product Name',)
    code = models.TextField(max_length=30, blank=True, default='', verbose_name='Product Code',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smartdoc:product_detail', args=[str(self.id)])

    @property
    def document_count(self):
        return Document.objects.filter(product_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "产品"


class Category(AbstractModel):
    """文档类型"""
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smartdoc:category_detail', args=[self.id])

    @property
    def document_count(self):
        return Document.objects.filter(category_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "文档分类"


class Document(AbstractModel):
    """文件"""
    title = models.TextField(max_length=30, verbose_name='Title',)
    version_no = models.IntegerField(blank=True, default=1, verbose_name='Version No.',)
    doc_file = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='documents',)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='documents', )

    def __str__(self):
        return self.title

    def get_format(self):
        return self.doc_file.url.split('.')[-1].upper()

    def get_absolute_url(self):
        return reverse('smartdoc:document_detail', args=[str(self.product.id), str(self.id)])

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "文档"

