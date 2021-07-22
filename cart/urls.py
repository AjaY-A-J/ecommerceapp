from django.conf.urls import url
from . import views
app_name='cart'


urlpatterns = [
    url(r'^',views.cart_detail,name="cart_detail"),
    url(r'^add/<int:product_id>/',views.add_cart,name="add_cart"),
    url(r'^remove/<int:product_id>/',views.cart_remove,name="cart_remove"),
    url(r'^full_remove/<int:product_id>/',views.full_remove,name="full_remove"),
    ]