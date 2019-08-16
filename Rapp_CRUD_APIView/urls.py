from django.conf.urls import url
from .import views
app_name='Rapp_CRUD_APIView'
urlpatterns = [
    url(r'^$',views.input),
    url(r'^link$',views.link),
    url(r'^display$',views.display),
    url(r'^product$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)$',views.ProductList1.as_view()),
]