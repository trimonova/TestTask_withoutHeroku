from django.conf.urls import url
from api import views
urlpatterns = [
    url(r'^menu/', views.menu, name='menu'),
    url(r'^order/create/?', views.order, name='order'),
    url(r'^login/?', views.user_login, name='user_login'),
    ]

    #url(r'^item/(?P<alias>[^/]+)', views.item, name='item'),
    #url(r'^cat/(?P<alias>[^/]+)', views.get_category, name='get_category'),
    #url(r'^order/', views.order, name='order'),


