from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<path>.+)$', views.get_post, name='get_post'),
    url(r'^posts$', views.list_posts, name='list_posts'),
]
