from django.conf.urls import url
from .import views
app_name='ecommerceapp'


urlpatterns = [
    url(r'^$',views.allProdCat,name='allProdCat'),
    url(r'^(?P<c_slug>\w+)/(?P<product_slug>\w+)/',views.ProdCatDetail,name='ProdCatDetail'),
    url(r'^(?P<c_slug>\w+)/',views.allProdCat,name='products_by_category'),

]