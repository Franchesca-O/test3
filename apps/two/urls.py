from django.conf.urls import url
from . import views           
urlpatterns = [
  url(r'^dashboard', views.dashboard, name = 'dashboard'),
  url(r'^create$', views.create, name = 'create'),
  url(r'^share/(?P<quote_id>\d+)$', views.share , name="share"),
  url(r'^remove/(?P<quote_id>\d+)$', views.remove , name="remove"),
  url(r'^logout$', views.logout , name="logout"),
  url(r'^summary/(?P<poster_id>\d+)$', views.summary, name ="summary"),
   url(r'^count$', views.count, name = 'count')
]