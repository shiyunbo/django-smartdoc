from django.forms import ModelForm,  TextInput, FileInput, Select
from .models import Product, Category, Document


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('author', 'create_date', 'mod_date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'code': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '产品名称',
            'code': '产品代码',
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('author', 'create_date', 'mod_date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '类别',
        }


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ('author', 'create_date', 'mod_date', 'product')

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'version_no': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'doc_file': FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '文档标题',
            'version_no': '版本号',
            'category': '文档类别',
            'doc_file': '上传文件',
        }

