from django.conf.urls import url
from django.urls import path, include
from products import views
from rest_framework import routers
from products.views import SingleProductView

router = routers.DefaultRouter()
router.register('products', views.ProductView)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>', SingleProductView.as_view()),
    url(r'^product/(?P<product_id>\d+)/$', views.product, name='product'),
]
