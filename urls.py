from django.urls import path, re_path
from . import views

# namespace
app_name = 'smartdoc'

urlpatterns = [

    # 展示产品列表
    path('product/', views.ProductList.as_view(), name='product_list'),

    # 展示产品详情
    re_path(r'^product/(?P<pk>\d+)/$',
            views.ProductDetail.as_view(), name='product_detail'),

    # 创建产品
    re_path(r'^product/create/$',
            views.ProductCreate.as_view(), name='product_create'),

    # 修改产品
    re_path(r'^product/(?P<pk>\d+)/update/$',
            views.ProductUpdate.as_view(), name='product_update'),

    # 展示类别列表
    path('category/', views.CategoryList.as_view(), name='category_list'),

    # 展示类别详情
    re_path(r'^category/(?P<pk>\d+)/$',
            views.CategoryDetail.as_view(), name='category_detail'),

    # 创建类别
    re_path(r'^category/create/$',
            views.CategoryCreate.as_view(), name='category_create'),

    # 修改类别
    re_path(r'^category/(?P<pk>\d+)/update/$',
            views.CategoryUpdate.as_view(), name='category_update'),

    # 展示文档列表
    path('document/', views.DocumentList.as_view(), name='document_list'),

    # 展示文档详情
    re_path(r'^product/(?P<pkr>\d+)/document/(?P<pk>\d+)/$',
            views.DocumentDetail.as_view(), name='document_detail'),

    # 创建文档
    re_path(r'^product/(?P<pk>\d+)/document/create/$',
            views.DocumentCreate.as_view(), name='document_create'),


    # 修改文档
    re_path(r'^product/(?P<pkr>\d+)/document/(?P<pk>\d+)/update/$',
            views.DocumentUpdate.as_view(), name='document_update'),

    # 文档搜索
    path('document/search/', views.document_search, name='document_search'),


    # Ajax搜索
    path('ajax/search/', views.doc_ajax_search, name='doc_ajax_search'),

]









