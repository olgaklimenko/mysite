from django.conf.urls import patterns, url
from photo_gallery import views

urlpatterns= patterns('',
    # ex: /photo_gallery/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #ex: /photo_gallery/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #ex: /photo_gallery/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(),name='results'),
    #ex: /photo_gallery/5/vote/
    url(r'^(?P<item_id>\d+)/vote/$', views.vote, name = 'vote'),
)
