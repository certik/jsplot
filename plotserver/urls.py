from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os.path
p = os.path.join(os.path.dirname(__file__), 'media_files/')

urlpatterns = patterns('plotserver.app.views',
        url(r'^$', 'index', name="index"),
        url(r'^raphael/$', 'raphael', name="raphael"),
        ) + \
    patterns('',
        (r'^media_files/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': p}),
    )
