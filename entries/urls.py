from django.conf.urls import patterns, url

urlpatterns = patterns('entries.views',
        url(r'^$', 'index', name='entries-all'),
        url(r'^entry/(\d+)/$', 'show_entry', name='entry-show'),
        url(r'^entry/add/$', 'create_entry', name='entry-create'),
        url(r'^entry/edit/(\d+)/$', 'edit_entry', name='entry-edit'))
