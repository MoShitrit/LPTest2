from django.conf.urls import url
from . import views

app_name = 'sites'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<lob>.*)/(?P<site_id>[0-9]+)/$', views.site, name='site'),
    url(r'^add_site$', views.add_site, name='add_site'),
    url(r'^site_added$', views.site_added, name='site_added')
]
