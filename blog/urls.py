from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    url(r'^blogger/(?P<pk>\d+)$', views.BloggerDetailView.as_view(), name='blogger-detail'),
    url(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    url(r'^(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
]