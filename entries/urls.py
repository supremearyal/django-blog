from django.conf.urls import patterns, url

urlpatterns = patterns('entries.views',
        url(r'^$', 'index', name='index'),
        url(r'^entry/(\d+)/$', 'show_entry', name='show_entry'),
        url(r'^entry/add/$', 'create_entry', name='create_entry'))
