from django.conf.urls import url
from . import views

app_name='searchapp'

urlpatterns = [
    url('^',views.searchresult,name='searchresult'),
    ]